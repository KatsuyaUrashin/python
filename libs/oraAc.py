# -*- coding: utf-8 -*-
# Oracleテーブルアクセスクラス
import sys
import oracledb
from socket import gethostname

DB_CONFIG = {'SAKUDELL-HT87G25': "localhost:1521/FREE",
             'MacA.local': "localhost:1521/FREEPDB1",
             }

class Table:
    """Oracleテーブルアクセスクラス
    """
    def __init__(self, tableName=None, db:Table=None, debug=False):
        """コンストラクタ

        Args:
            tableName (str, optional): テーブル名. Defaults to None.
            db (Table, optional): テーブルアクセスハンドル(テーブル違いで同じセッション利用). Defaults to None.
            debug (bool, optional): デバッグするか. Defaults to False.
        """
        self.debug = debug
        # テーブルアクセスハンドルがあればそれを利用、なければ新規に接続
        if db is not None:
            self.connection = db.connection
            self.newConnection = False
        else:
            self.connection = self._get_connection()
            self.newConnection = True
        self.tableName = tableName
        # SQLファイルを読み込む
        self.sqls = {}
        for queryType in ["select", "insert", "delete", "update"]:
            self.sqls[queryType] = self._readSqlFile(queryType)
        self.tranFlag = False

    def _getTemplateSqlFileName(self, queryType):
        """SQLファイル名取得

        Args:
            queryType (str): SQLのタイプ

        Returns:
            str: SQLファイル名
        """
        if self.tableName is None:
            raise ValueError("tableName must be provided")
        return f"sql/{self.tableName}-{queryType}.sql"

    def _readSqlFile(self, queryType):
        """SQLファイル読み込み

        Args:
            queryType (str): SQLのタイプ

        Raises:
            ValueError: 値のエラー

        Returns:
            str: 読み込んだSQL文字列(ファイルがなければNone)
        """
        if self.tableName is None:
            raise ValueError("tableName must be provided")
        filePath = self._getTemplateSqlFileName(queryType)
        try:
            with open(filePath, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            # raise FileNotFoundError(f"SQL file not found: {filePath}")
            return None

    def _get_connection(self):
        """接続情報取得

        Returns:
            any: 接続情報
        """
        hostname = gethostname()
        dbConfig = DB_CONFIG.get(hostname)
        return oracledb.connect(
            user="system",
            password="oracle123",
            dsn = dbConfig,   # ← これが一番シンプル
            # 必要なら以下を追加
        # config_dir="/path/to/wallet",   # Autonomous DB用
    )
    def __enter__(self):
        return self 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.newConnection:
            if self.tranFlag:
                self.connection.rollback()
            self.connection.close()
            self.newConnection = False 
    def commit(self):
        self.connection.commit()
        self.tranFlag = False
    def rollback(self):
        self.connection.rollback()
        self.tranFlag = False
    def _printDebugSql(self, sqlString, params):
        if self.debug:
            print("Executing SQL:")
            print(sqlString)
            print("With parameters:")
            print(params)

    def _makeSqlString(self, queryType, params):
        """指定のパラメータでSQL文字列を作成する。
        辞書にないバインド変数は行コメントにする

        Args:
            queryType (str): クエリのタイプ(select, insert, delete, update)
            params (辞書): パラメータ

        Returns:
            str: 作成したSQL
        """
        # SQLで指定のパラメータのみ条件に残す
        sqlString = self.sqls.get(queryType)
        if sqlString is None:
            print(f"SQL template file({self._getTemplateSqlFileName(queryType)}) for '{queryType}' is None")
            sys.exit(1)
        for key in params.keys():
            # 置換対象ががない場合はエラーで終了
            if f"/*${key}*/" not in sqlString:
                print(f"Parameter '{key}' is not found in SQL template") 
                sys.exit(1)
            sqlString = sqlString.replace(f"/*${key}*/", f"   /*{key}*/")  # パラメータがあればそのまま
        # 残った物はコメントアウト
        sqlString = sqlString.replace("/*$", "-- /*")
        self._printDebugSql(sqlString, params)
        return sqlString
    
    def select(self, **params):
        """検索実行

        Returns:
            辞書の配列: 取得結果
        """
        # SQLで指定のパラメータのみ条件に残す
        sqlString = self._makeSqlString("select", params)
        with self.connection.cursor() as cursor:
            cursor.execute(sqlString, **params)
            columns = [col.name for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            return cursor.fetchall()

    def _execute(self, queryType, **params):
        """実行

        Args:
            queryType (str): クエリのタイプ

        Returns:
            dic: {テーブル名: 件数}
        """
        sqlString = self._makeSqlString(queryType, params)
        with self.connection.cursor() as cursor:
            cursor.execute(sqlString, **params)
            self.tranFlag = True
            return {self.tableName: cursor.rowcount}

    def insert(self, **params):
        """登録実行
        """
        return self._execute("insert", **params)

    def delete(self, **params):
        """削除実行
        """
        return self._execute("delete", **params)

    def update(self, **params):
        """更新実行
        """
        return self._execute("update", **params)

def getArgs(argv, minArgs=2):
    """引数を取得

    Args:
        argv (list): 引数(sys.argv)プログラム名 テーブル名 任意のキー:値ペア --debug
        minArgs (int, optional): 最低引数の数. Defaults to 2.

    Returns:
        str, dict, debug: テーブル名, 項目の辞書, デバッグフラグ
    """
    keyValueStr0 = "<key:value> "
    keyValueStr = keyValueStr0 * (minArgs - 2)
    errMessage = f"Usage: python {argv[0]} <tableName> {keyValueStr}[{keyValueStr0}...] [allset] [--debug]"
    # 引数の数は、テーブル名 + 任意のキー:値ペアでminArgs以上でなければエラー
    if minArgs > len(argv):
        print(errMessage)
        sys.exit(1)

    # 第一引数はテーブル名
    tableName = argv[1].upper()  # テーブル名は大文字に変換
    
    keys = {}
    debug = False
    for arg in argv[2:]:
        if arg == "--debug":
            debug = True
        elif arg == "allset":
            # allsetが指定された場合、キー:値ペアは不要
            pass
        else:   
            keyValue = arg.split(":")
            if len(keyValue) != 2:
                print(errMessage)
                sys.exit(1)
            key, value = keyValue
            #  SHIMEIならアンダースコアを空白にする
            keys[key.upper()] = value
    return tableName, keys, debug
