# def func(a, b, c):
#     print(f"a: {a}, b: {b}, c: {c}")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"値は{a}です。")
sum = 0
for val in a:
    sum = sum + val
    print(f"val:{val}, sum:{sum}")
print(f"合計は{sum}です。")
a[0] = 2    # ０番目を変更する
a[2] = 6
# a.append(5)
# a = "10-2"
# print(f"値は{a}です。")
# func(*a)

