# マップ処理

# グローバル変数
KEYS = None

# Alt+←(左矢印)で戻れるよ
def procMap(i, data, option):
    global KEYS
    if i == 0:
        # キーの作成
        KEYS = data
        return None
    else:
        # 辞書を作成
        jisho = {key: data[j] for j, key in enumerate(KEYS)}
        option['count'] += 1

        # jisho = {}
        # for j, key in enumerate(keys):
        #     jisho |= {key: data[j]}

        return jisho
