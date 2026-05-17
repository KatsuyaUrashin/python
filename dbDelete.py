#!/usr/bin/env python3
# コマンドライン引数でテーブル名と任意のキー:値ペアを受け取り、テーブルから行を削除するスクリプト
import sys
from libs.OraAc import Table, getArgs

def main():
    # コマンドライン引数からテーブル名とキー:値ペアを取得
    # 最低でもテーブル名と1つのキー:値ペアが必要なので、minArgs=3を指定
    # ただし、allsetを指定している場合は、キー:値ペアがなくてもテーブル名だけで削除できるようにする
    tableName, keys, debug = getArgs(sys.argv, minArgs=2)
    with Table(tableName=tableName, debug=debug) as conn:
        conn2 = Table(tableName='LOG', db=conn)
        ret = conn.delete(**keys)
        conn2.insert({
            "OPERATION": "DELETE",
            "TABLE_NAME": tableName,
            "KEYS": str(keys),
            "RESULT": str(ret)
        })
        print(f"Delete result: {ret}")
        conn.commit()
        sys.exit(0)

if __name__ == '__main__':
    main()

