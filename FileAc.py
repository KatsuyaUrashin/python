# ファイルアクセスクラス
class FIL:
    # コンストラクタ
    def __init__(self, fName, enc='utf-8', delimt='|'):
        # ファイルをオープン
        self.fn = fName
        self.enc = enc
        self.delimt = delimt

    def __enter__(self):
        print(f"[{self.fn}] 前処理: 開始")
        self.fp = open(file=self.fn, encoding=self.enc)
        return self  # as節で受け取る値

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[{self.fn}, exc_type:{exc_type}, exc_val:{exc_val}, exc_tb:{exc_tb}] 後処理: 終了")
        # ここで例外処理を行うことも可能
        print(f"[{self.fn}]ファイルをクローズする")
        self.fp.close()
        print(f"テーブルにインサートしてコミットする。")

    def readLine(self):
        # 行を読み込んで分割して空白除去
        return [[d.strip() for d in line.split(self.delimt)] for line in self.fp]
