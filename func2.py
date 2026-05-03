# -*- coding: utf-8 -*-
# 関数の練習
def func2(a):
    a[1] = 6
    return a[0] * a[2]
#####################
x = [8, 2, 3]
print(f"func2呼ぶ　前x={x}")

y = func2(x)
print(f"{x[0]}*{x[2]}の答え、y={y}")

print(f"func2呼んだ後x={x}")
