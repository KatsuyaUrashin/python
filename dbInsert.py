#!/usr/bin/env python3
# コマンドライン引数でテーブル名と任意のキー:値ペアを受け取り、テーブルに行を挿入するスクリプト
import sys
from libs.OraAc import Table, getArgs

def main():
    # コマンドライン引数からテーブル名とキー:値ペアを取得
    tableName, keys, debug = getArgs(sys.argv, minArgs=3)
    # データベーステーブルに接続して行を挿入
    with Table(tableName=tableName, debug=debug) as conn:
        ret = conn.insert(**keys)
        print(f"Insert result: {ret}")
        conn.commit()
        sys.exit(0)

if __name__ == '__main__':
    main()

