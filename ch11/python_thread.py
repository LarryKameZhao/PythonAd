#操作系统能调度的最小单元是线程
#对于IO操作来说，多线程和多进程性能差距不大
#通过Thread类实例化
import threading
import time

#通过继承Thread来继承多线程

class GetDetailHTML(threading.Thread):

    def __init__(self,name):
        super().__init__(name=name)
    def run(self):
        print('get detail_html started')
        time.sleep(2)
        print('get detail-html end')

class GetDetailUrl(threading.Thread):
    def __init__(self,name):
        super().__inti__(name=name)
    def run(self):
        print('get detail_url started')
        time.sleep(4)
        print('get detail-url end')

if __name__ == '__main__':
    thread1 = GetDetailHTML('get_detail_html')
    thread2 = GetDetailUrl('get_detail_url')
    start_time = time.time()
    #守护线程，设为守护线程后，主线程会等待知道守护线程执行完成
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    thread1.start()
    thread2.start()
    # join方法阻塞线程，直到两个线程执行完成后才会运行后面的程序
    thread1.join()
    thread2.join()

    #当主线程推出的时候，子线程kill掉
    print('last time:{}'.format((time.time()-start_time)))

