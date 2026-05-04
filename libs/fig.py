# -*- coding: utf-8 -*-
# 図形クラスのコード
# # fig
import sys

# 図形クラス(三角形クラスとかのスーパークラス＝親クラス)
class Fig:
    # コンストラクター(クラスを作る時のお決まりの関数)
    # 引数の頭のselfはクラスの関数の場合には必要
    def __init__(self, name):
        self.name = name
    def GetName(self):
        return self.name

# 三角形クラス(Figの派生クラス)
class Tri(Fig):
    # コンストラクター(クラスを作る時のお決まりの関数)
    # 引数の頭のselfはクラスの関数の場合には必要
    def __init__(self, bottom, height):
        super().__init__("三角形")
        self.bottom = bottom   # 底辺
        self.height = height   # 高さ
    # 面積を計算する
    def area(self):
        return self.bottom * self.height / 2

    # 周囲の長さ
    def length(self):
        return self.bottom + self.height + 3

# 長方形クラス(Figの派生クラス)
class Squ(Fig):
    # コンストラクター(クラスを作る時のお決まりの関数)
    # 引数の頭のselfはクラスの関数の場合には必要
    def __init__(self, bottom, height):
        super().__init__("長方形")
        self.bottom = bottom   # 底辺
        self.height = height   # 高さ
        self.bai = 2
    # 面積を計算する
    def area(self):
        return self.bottom * self.height
    # 周囲の長さ
    def length(self):
        return (self.bottom + self.height) * self.bai 

if __name__ == '__main__':
    z = sys.argv
    # print(f"引数は、{z}")
    # print(f"引数１番目{sys.argv[1]}")
    # クラスの実体化=オブジェクト作成=インスタンス化
    y = Tri(3, 4)
    x = [
        Tri(1, 2),  # 三角形
        Squ(3, 4),  # 長方形
    ]
    # 未処理
    noUse = True
    # 引数の指定がないときは全部処理する
    for d in x:
        # 引数の指定ないとき、または、引数の指定と名前が同じときに印字
        if len(sys.argv) == 1 or sys.argv[1] == d.GetName():
            noUse = False
            print(f"{d.GetName()}の面積は{d.area()}, 周囲の長さは{d.length()}")
    if noUse:
        print("そんなのないよ")