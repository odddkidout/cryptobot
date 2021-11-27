import threading
import time

class Engine:
    def __init__(self):
        self.running = False
        self.thread = None
        self.thread_lock = threading.Lock()

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def run(self):
        while self.running:
            time.sleep(1)
            print("Engine running")