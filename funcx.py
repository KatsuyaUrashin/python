# funcx.py
# 関数Xの定義
def funcC(x):
    return x * 3

def funcAB(a, b):
    c = funcC(a)
    return a * b * c

def funcA_plus_B(a, b):
    return a + b

def testMain():
    print(f"テストA={funcAB(2, 3)}")
    print(f"テストB={funcA_plus_B(2, 3)}")

# 関数としての確からさの確認(テストドライバー)
if __name__ == '__main__':
    testMain()
