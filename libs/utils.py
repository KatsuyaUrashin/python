# プロセス管理クラス
import datetime

class ProcessManager:
    def __init__(self):
        self.start_time = datetime.datetime.now()

    def start_process(self):
        print(f"========== プロセスを開始します。 ========== {self.start_time.strftime('%Y/%m/%d %H:%M:%S')}")
    
    def end_process(self):
        end_time = datetime.datetime.now()
        elapsed_time = end_time - self.start_time
        print(f"========== プロセスを終了します。 ========== {end_time.strftime('%Y/%m/%d %H:%M:%S')} (経過時間: {elapsed_time})")
