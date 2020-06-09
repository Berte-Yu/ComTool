import threading
class thread():
    def __init__(self, run_func):
        self.thread = threading.thread(target=self.run)
        self.__flag = threading.Event()         # 用于暂停线程的标识
        self.__flag.set()                       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()                    # 将running设置为True
        self.__run_func = run_func

    def start(self):
        self.thread.start()
    
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            self.__run_func()

    def pause(self):
        self.__flag.clear()         # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()           # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__running.clear()      # 设置为False
        self.__flag.set()           # 将线程从暂停状态恢复, 如何已经暂停的话
        

if __name__ == "__main__":
    import time
    def run1():
        time().sleep(1)
        print("run1 sleep 1s.")

    t1 = thread(run1)
    t1.start()
    time().sleep(8)
    t1.pause()
    print("阻塞了")
    time().sleep(10)
    t1.resume("解除了")
