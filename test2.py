man = {"年齢": 35, "身長": 145, '4': 20}
key = '身長'
man[key] = 172
man['4'] = 64
print(f"パパ: {key}{man[key]}")
key = '年齢'
print(f"パパ: {key}{man[key]}")
print(f"パパ: {man}")
s = ""
for k, v in man.items():
    c = "パパ:" if s == "" else ","
    # 左辺 = 右辺　右辺の値を計算して左辺に入れる代入文
    # 左辺(代入される変数) = 右辺[真の時の値　if 条件 else 偽の時の値]代入する値
    s += f"{c} {k}:{v}"
print(s)
s = ""
for k, v in man.items():
    s += f"{'パパ:' if s == '' else ','} {k}:{v}"
print(s)
print([f"{k}:{v}" for k, v in man.items()])
print([y*2 for y in (1, 2, 3)])
print(",".join(["1", "2", "3"]))
l = ["a", "b", "c"]
print(l, ",   ".join(x for x in l))
print(l, ",   ".join(x+x for x in l))

man = {"年齢": 35, "身長": 145, '4': 20}
s = 'パパ: ' + ", ".join(f"{k}={v}" for k, v in man.items())
print(s)
s = 'パパ: ' + ", ".join(man.keys())
print(s)

# ---start
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for i, data in enumerate(a):
    # 偶数, 奇数
    val = "偶数" if data % 2 == 0 else "奇数"
    # 倍数
    for j, bai in enumerate(range(3, 6)):
        if data % bai == 0:
            val = val + f"でかつ、{j+1}:{bai}の倍数"
    print(f"{i+1}, {val}：{data}")
