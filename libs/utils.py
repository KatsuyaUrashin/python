# プロセス管理クラス
import datetime

class ProcessManager:
    def __init__(self):
        self.started = False

    def start_process(self):
        self.start_time = datetime.datetime.now()
        print(f"========== プロセスを開始します。 ========== {self.start_time.strftime('%Y/%m/%d %H:%M:%S')}")
        self.started = True
    
    def end_process(self):
        if self.started:
            end_time = datetime.datetime.now()
            elapsed_time = end_time - self.start_time
            print(f"========== プロセスを終了します。 ========== {end_time.strftime('%Y/%m/%d %H:%M:%S')} (経過時間: {elapsed_time})")
