#!/usr/bin/env python3
# コマンドライン引数でテーブル名と任意のキー:値ペアを受け取り、テーブルから行を削除するスクリプト
import sys
from libs.oraAc import Table, getArgs

def main():
    # コマンドライン引数からテーブル名とキー:値ペアを取得
    # 最低でもテーブル名と1つのキー:値ペアが必要なので、minArgs=3を指定
    # ただし、allsetを指定している場合は、キー:値ペアがなくてもテーブル名だけで削除できるようにする
    tableName, keys, debug = getArgs(sys.argv, minArgs=3)
    with Table(tableName=tableName, debug=debug) as conn:
        ret = conn.delete(**keys)
        print(f"Delete result: {ret}")
        conn.commit()
        sys.exit(0)

if __name__ == '__main__':
    main()

