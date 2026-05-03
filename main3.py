# main3.py
from funcx import funcAB, funcA_plus_B

def main():
    # 辞書3個の配列
    fns = [
        {
            'fnc':  funcAB,
            'a':    30,
            'b':    50,
        },
        {
            'fnc':  funcA_plus_B,
            'a':    20,
            'b':    40,
        },
        {
            'fnc':  funcAB,
            'a':    1,
            'b':    2,
        },
    ]
    for data in fns:
        # x = funcAB(30, 50)
        # x = funcA_plus_B(20, 40)
        # x = funcAB(1, 2)
        x = data['fnc'](data['a'], data['b'])
        print(f"{data['fnc'].__name__}(a:{data['a']}, b:{data['b']}), x={x}")

if __name__ == '__main__':
    main()

