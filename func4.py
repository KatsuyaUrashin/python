def func4(a, m='+', b=0):   # =をつけるとデフォルト値指定
    try:
        if m == '*':
            return a * b
        elif m == '+':
            return a + b
        elif m == '/':
            try:
                if b == 0:
                    return None
                return a / b
            finally:
                print("割った後")
        else:
            return None
    except ZeroDivisionError:
      print(f"０で割りました")
      return None
    except Exception as e:
       print(f"予期せぬエラーです。{e}")
       return None
    finally:
        # ファイルをオープンしていたときとか、
        # DBのテーブルアクセスした後に、コミットとかロールバックするため
        print("最後の処理")
#####################
x = [8, 2, 3]

y = func4(x[0], b=x[2])
print(f"1. {x[0]}*{x[2]}の答え、y={y}")

y = func4(x[0], '*', x[2])
print(f"2. {x[0]}*{x[2]}の答え、y={y}")

y = func4(x[0], b=x[2], m='*')
print(f"2. {x[0]}*{x[2]}の答え、y={y}")

y = func4(x[0])
print(f"3. {x[0]}+{x[2]}の答え、y={y}")

y = func4(x[0], m='/')
print(f"4. {x[0]}*{x[2]}の答え、y={y}")
