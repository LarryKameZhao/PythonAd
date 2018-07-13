from threading import Lock

import threading
#from threading import RLock
#用锁会影响性能，锁会引起死锁
#在同一个线程里面，可以连续调用多次acquire，acquire（）次数要和release（）相同

total = 0
lock = Lock()
def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total +=1
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()



thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
