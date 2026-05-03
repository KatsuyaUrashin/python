#!/usr/bin/env python3
# コマンドライン引数でテーブル名と任意のキー:値ペアを受け取り、テーブルに行を挿入するスクリプト
import sys
from libs.Oracle import Table, getArgs

def main():
    tableName, keys, debug = getArgs(sys.argv, "dbInsert.py", minArgs=3)
    with Table(tableName=tableName, debug=debug) as conn:
        ret = conn.insert(**keys)
        print(f"Insert result: {ret}")
        conn.commit()
        sys.exit(0)

if __name__ == '__main__':
    main()

