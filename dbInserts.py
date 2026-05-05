#!/usr/bin/env python3
# パラメータからテーブル名とファイル名を受け取って、ファイルの内容をテーブルにインサートするコード
import sys
from libs.oraAc import Table, getFileArgs
from libs.FileAc import FIL
from maps.map1 import procMap

def main():
    tableName, fileName, debug = getFileArgs(sys.argv)
    option = {"tableName": tableName, "fileName": fileName, "debug": debug, 'count': 0}
    with Table(tableName=tableName, debug=debug) as conn:
        with FIL(fName=fileName, delimt=",", enc='utf-8-sig') as fp:
            for i, data in enumerate(fp.readLine()):
                data = procMap(i, data, option)  # データをマッピング
                if data is not None:
                    ret = conn.insert(data)
                    if debug:
                        print(f"line {i}: {ret}")
        conn.commit()
        sys.exit(0)

if __name__ == '__main__':
    main()

