#!/usr/bin/env python3
# コマンドライン引数でテーブル名と任意のキー:値ペアを受け取り、テーブルから行を削除するスクリプト
import sys
from libs.Oracle import Table, getArgs

def main():
    tableName, keys, debug = getArgs(sys.argv, minArgs=3)
    with Table(tableName=tableName, debug=debug) as conn:
        ret = conn.delete(**keys)
        print(f"Delete result: {ret}")
        conn.commit()
        sys.exit(0)

if __name__ == '__main__':
    main()

