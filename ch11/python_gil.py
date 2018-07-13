#GIL global interpreter lock
#python中一个线程对应c语言一个线程
#GIL使得同一时刻只有一个线程运行在一个cpu上执行字节码,无法将多个线程映射到多cpu上执行
#GIL会根据执行字节码行数以及时间片来自动释放；遇到IO操作也会释放
total = 0

def add():
    global total
    for i in range(1000000):
        total +=1

def desc():
    global total
    for i in range(1000000):
        total -= 1

import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)


