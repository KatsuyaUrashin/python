#!/usr/bin/env python3
# コマンドライン引数でテーブル名と任意のキー:値ペアを受け取り、テーブルから行を削除するスクリプト
import sys
from libs.OraAc import Table, getArgs

def main():
    # コマンドライン引数からテーブル名とキー:値ペアを取得
    # 最低でもテーブル名と1つのキー:値ペアが必要なので、minArgs=3を指定
    # ただし、allsetを指定している場合は、キー:値ペアがなくてもテーブル名だけで削除できるようにする
    tableName, keys, user, debug = getArgs(sys.argv, minArgs=2)
    with Table(tableName=tableName, user=user, debug=debug) as conn:
        # conn2 = Table(tableName='OPERATE_LOG', db=conn)
        ret = conn.delete(**keys)
        """
        # 削除結果をログテーブルに記録
        ret2 = conn2.insert({
            "OPERATION": "DELETE",
            "USE_TABLE": tableName,
            "KEYS": str(keys),
            "RESULT": str(ret),
            "OPERATION_USER": user,
        })
        # conn2はコミットしないがフラッシュが必要
        conn2.flush()  # バルクインサートの残りをフラッシュする（これ実際に業務では忘れている）
        print(f"Log insert result: {ret2}")
        """
        conn.commit()
        print(f"Delete result: {ret}")
        sys.exit(0)

if __name__ == '__main__':
    main()

