# -*- coding: utf-8 -*-
# エンジンのコード
import sys
# from sys import argv
from libs.FileAc import FIL
# import map1
from maps.map1 import procMap
CRLF = "\n"
fname = sys.argv[1]
option = {
    'count': 0,
}
# ファイルを開いて、行ごとに処理する
with FIL(fName=fname, delimt=",") as fp:
    for i, data in enumerate(fp.readLine()):
        # １行の行末の改行を削ってカンマで分割して配列にして
        ret = procMap(i, data, option)  # F12で定義に飛ぶよ
        if i != 0:
            print(f"line {i}: {ret}")

print(f"count:{option['count']}")