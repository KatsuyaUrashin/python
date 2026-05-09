# -*- coding: utf-8 -*-
# ファイルアクセスのコード
class FIL:
    """ファイルアクセスクラス

    Returns:
        FIL: ファイルアクセスクラス
    """
    # ファイルアクセスのクラス
    def __init__(self, fName, enc='utf-8', delimt='|'):
        # ファイルをオープン
        self.fn = fName
        self.enc = enc
        self.delimt = delimt

    # with構文で使うためのメソッド
    def __enter__(self):
        print(f"***** [{self.fn}] 前処理: 開始 *****")
        self.fp = open(file=self.fn, encoding=self.enc)
        return self  # as節で受け取る値

    # with構文で使うためのメソッド
    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(f"[{self.fn}, exc_type:{exc_type}, exc_val:{exc_val}, exc_tb:{exc_tb}] 後処理: 終了")
        # ここで例外処理を行うことも可能
        print(f"***** [{self.fn}]ファイルをクローズしました。 *****")
        self.fp.close()

    # ファイルを行ごとに読み込むメソッド
    def readLine(self):
        """ファイルを行毎に読み込む
            ・行を分割して空白を除去してリストに格納する

        Returns:
            [str]: 読み込んだデータ
        """
        # 行を読み込んで分割して空白除去
        return [[d.strip() for d in line.split(self.delimt)] for line in self.fp]
