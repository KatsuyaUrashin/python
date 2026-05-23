#!/usr/bin/env python3
# パラメータからテーブル名とファイル名を受け取って、ファイルの内容をテーブルにインサートするコード
import sys
from libs.OraAc import Table, getFileArgs
from libs.FileAc import FIL
from maps.map1 import procMap
from libs.utils import ProcessManager

def main():
    process_manager = ProcessManager()
    try:
        tableName, fileName, user, debug = getFileArgs(sys.argv)
        process_manager.start_process()
        option = {"tableName": tableName, "fileName": fileName, "debug": debug, 'count': 0}
        with Table(tableName=tableName, user=user, debug=debug) as conn:
            try:
                with FIL(fName=fileName, delimt=",", enc='utf-8-sig') as fp:
                    for i, data in enumerate(fp.readLine()):
                        data = procMap(i, data, option)  # データをマッピング
                        if data is not None:
                            ret = conn.insert(data)
                            if debug:
                                print(f"line {i}: {ret}")
                """
                conn2 = Table(tableName='OPERATE_LOG', db=conn, debug=debug)
                ret2 = conn2.insert({
                    "OPERATION": "INSERT",
                    "USE_TABLE": tableName,
                    "RESULT": f"Inserted from {fileName}, total {option['count']} rows",
                    "OPERATION_USER": user,
                })
                # conn2はコミットしないがフラッシュが必要
                conn2.flush()  # バルクインサートの残りをフラッシュする（これ実際に業務では忘れている）
                print(f"Insert result: {ret}")
                print(f"Log insert result: {ret2}")
                """
                conn.commit()
            except Exception as e:
                print(f"Error occurred: {e}")
                conn.rollback()
            sys.exit(0)
    finally:
        process_manager.end_process()

if __name__ == '__main__':
    main()

