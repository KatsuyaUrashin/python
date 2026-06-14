# 成績のマップ処理

# グローバル変数
KEYS = ('GAKUSEKI_NO', 'MATH_SCORE', 'ENGLISH_SCORE', 'JAPANESE_SCORE')

# Alt+←(左矢印)で戻れるよ
def procMap(i, data, option):
    global KEYS
    if i == 0:
        print(f"data: {data}")
        return None
    else:
        # ファイルから読み込んだ成績を設定
        jisho = {key: (int(data[j]) if data[j].strip() != '' else None) if key.endswith('_SCORE') else data[j] for j, key in enumerate(KEYS)}

        # AI # 有効なスコアだけのリストを1行で作る
        # AI scores = [jisho[key] for key in KEYS if key.endswith('_SCORE') and jisho[key] is not None]
        # AI # そのリストの合計と件数を加算する
        # AI sumScore = sum(scores)
        # AI devideNum = len(scores)

        # 私 合計値と平均値を求める
        sumScore = 0
        devideNum = 0
        for key in KEYS:
            if key.endswith('_SCORE'):
                if jisho[key] is not None:
                    sumScore += jisho[key]
                    devideNum += 1
        
        # AIまたは私 その結果をjishoに追加する
        jisho['SUM_SCORE'] = sumScore
        jisho['AVG_SCORE'] = (sumScore / devideNum) if devideNum > 0 else None
        option['count'] += 1




        # jisho = {}
        # for j, key in enumerate(keys):
        #     jisho |= {key: data[j]}

        return jisho
