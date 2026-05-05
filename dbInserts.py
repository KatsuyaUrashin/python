#!/usr/bin/env python3
# パラメータからテーブル名とファイル名を受け取って、ファイルの内容をテーブルにインサートするコード
import sys
from libs.oraAc import Table, getFileArgs
from libs.FileAc import FIL
from maps.map1 import procMap
from libs.utils import ProcessManager

def main():
    process_manager = ProcessManager()
    try:
        tableName, fileName, debug = getFileArgs(sys.argv)
        option = {"tableName": tableName, "fileName": fileName, "debug": debug, 'count': 0}
        with Table(tableName=tableName, debug=debug) as conn:
            try:
                with FIL(fName=fileName, delimt=",", enc='utf-8-sig') as fp:
                    for i, data in enumerate(fp.readLine()):
                        data = procMap(i, data, option)  # データをマッピング
                        if data is not None:
                            ret = conn.insert(data)
                            if debug:
                                print(f"line {i}: {ret}")
                conn.commit()
            except Exception as e:
                print(f"Error occurred: {e}")
                conn.rollback()
            sys.exit(0)
    finally:
        process_manager.end_process()

if __name__ == '__main__':
    main()

