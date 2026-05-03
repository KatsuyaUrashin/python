def func3(a, key='リンゴ'):
    try:
        if type(a) is int:
            print("数字はだめです。")
            return (None, "NG", 1)
        a['みかん'] = 6
        return a[key] * a['バナナ'], '計算しました。', 3
    #except KeyError:
    #    print(f"キー<<{key}>>がない。")
    #    return None, "aa", 0
    except Exception as e:
        print(f"例外<<{type(e).__name__}, {e}>>")
        return None, "例外", 0
#####################
x = {'リンゴ': 8,
     'みかん': 2,
     'バナナ': 3,
}
print(f"func2呼ぶ　前x={x}")

y, mes, _ = func3(x, "リンゴa")
print(f"リンゴ{x['リンゴ']}*バナナ{x['バナナ']}の答え、y={y}, {mes}")
y = func3(3)
print(f"リンゴ{x['リンゴ']}*バナナ{x['バナナ']}の答え、y={y}")

print(f"func2呼んだ後x={x}")
