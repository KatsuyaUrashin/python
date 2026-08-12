# プロセス管理クラス
import datetime

class ProcessManager:
    # プロセスの開始を管理するクラス
    def __init__(self):
        self.started = False
    
    # With文の開始時に呼び出されるメソッド
    def __enter__(self):
        self.start_time = datetime.datetime.now()
        print(f"========== プロセスを開始します。 ========== {self.start_time.strftime('%Y/%m/%d %H:%M:%S')}")
        self.started = True
        return self 

    # With文の終了時に呼び出されるメソッド
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.started:
            end_time = datetime.datetime.now()
            elapsed_time = end_time - self.start_time
            print(f"========== プロセスを終了します。 ========== {end_time.strftime('%Y/%m/%d %H:%M:%S')} (経過時間: {elapsed_time})")
