# funcx.py
# 関数Xの定義

# 入力値を3倍にして返す
def funcC(x):
    return x * 3

# aにfuncC(a)の結果を乗じ、さらにbを乗じた値を返す
def funcAB(a, b):
    c = funcC(a)
    return a * b * c

# aとbを加算して返す
def funcA_plus_B(a, b):
    return a + b

# テスト実行関数
def testMain():
    print(f"テストA={funcAB(2, 3)}")
    print(f"テストB={funcA_plus_B(2, 3)}")

# 関数としての確からさの確認(テストドライバー)
if __name__ == '__main__':
    testMain()
