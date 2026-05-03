# ファイル読み込み
import sys
CRLF = "\n"
fname = sys.argv[1]
# 後で辞書型のデータを入れる配列を初期化
results = []
with open(file=fname, encoding='utf-8') as fp:
    for i, line in enumerate(fp):
        # １行の行末の改行を削ってカンマで分割して配列にして
        data = [d.strip() for d in line.split("|")]
        if i == 0:
            # キーの作成
            keys = data
        else:
            # 辞書を作成
            jisho = {key: data[j] for j, key in enumerate(keys)}

            # jisho = {}
            # for j, key in enumerate(keys):
            #     jisho |= {key: data[j]}

            # 結果sに辞書を追加
            results.append(jisho)

# 読み込んだ後に結果の印字
for i, d in enumerate(results, 1):
    print(f"line {i}:{d}")
