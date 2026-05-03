# ファイル読み込み
import sys
# from sys import argv
from FileAc import FIL
# import map1
from maps.map1 import procMap
CRLF = "\n"
fname = sys.argv[1]
option = {
    'count': 0,
}
with FIL(fName=fname, delimt=",") as fp:
    for i, data in enumerate(fp.readLine()):
        # １行の行末の改行を削ってカンマで分割して配列にして
        ret = procMap(i, data, option)  # F12で定義に飛ぶよ
        if i != 0:
            print(f"line {i}: {ret}")
#fp = FIL(fName=fname)
#fp.__enter__()
#fp.__exit__(1, 2, 3)

print(f"count:{option['count']}")