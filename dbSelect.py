 #!/usr/bin/env python3
# コマンドライン引数でテーブル名と任意のキー:値ペアを受け取り、テーブルから条件に合う行を選択して表示するスクリプト
import sys
from libs.OraAc import Table, getArgs

def main():
    tableName, keys, user, debug = getArgs(sys.argv)
    # テーブルから条件に合う行を選択して表示
    with Table(tableName=tableName, user=user, debug=debug) as conn:
        for i, row in enumerate(conn.select(**keys), start=1):
            print(f"{i}: {row}")

if __name__ == '__main__':
    main()

