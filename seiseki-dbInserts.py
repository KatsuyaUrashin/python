#!/usr/bin/env python3
# パラメータからテーブル名とファイル名を受け取って、ファイルの内容をテーブルにインサートするコード
import sys
from libs.OraAc import Table, getFileArgs2
from libs.FileAc import FIL
from maps.mapSeiseki import procMap
from libs.utils import ProcessManager

def main():
    process_manager = ProcessManager()
    try:
        fileName, user, debug = getFileArgs2(sys.argv)
        process_manager.start_process()
        option = {"tableName": 'SEISEKI', "fileName": fileName, "debug": debug, 'count': 0}
        with Table(tableName='SEISEKI', user=user, debug=debug) as conn:
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

