# 関数の練習

# (123)[1, 2, 3]

# 実z → アドレス(123)
#      ↓コピー　　      ↑
# 仮v → アドレス(123)　↑
# 
# 実z → 30
#      ↓コピー　　↑
# 仮v → 30
# 　　　40
# 
# v(123)[1] = 333
#     [1, 333, 2]
# v = アドレス(123)
# v = 「アドレス」中身
# v = "aaa"  ←アドレスが消えて"aaa"に置き換わる
# v = 「文字列」中身
# v[0] =　つまり、「アドレス」[0] = 

# 関数の定義
def func(x, m, y, v):  # 仮引数: x, m, y, v
    print(f"...前 func(z->v:{v})")
    v.append(m)
    print(f"...後 func(v:{v})")
    if m == '*':
        return x * y
    elif m == '/':
        return x / y
    elif m == '+':
        return x + y
    elif m == '-':
        return x - y
    else:
        return "error"

# スタート
x = 10
y = 5
key = '*'
z = ["モード", "zzz", 'qqq']
w = z[1:]
w[0] = "vvv"
print(f"w={w}")
print(f"1func前z={z}")
print(f"2答え＝{func(10, '*', 5, z)}")   # 実引数: x, key, y
print(f"3func後z={z}")
print(f"4答え＝{func(30, '/', 3, z)}")
print(f"5func後z={z}")
print(f"6答え＝{func(22, '/', 2, z)}")
print(f"7func後z={z}")
key = '+'
print(f"8答え＝{func(x, key, y, z)}")
print(f"9func後z={z}")
key = '-'
print(f"10答え＝{func(x, key, y, z)}")
print(f"11func後z={z}")
key = 'x'
print(f"12答え＝{func(x, key, y, z)}")
print(f"13func後z={z}")
