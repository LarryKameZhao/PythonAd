#多进程编程
#耗cpu的操作，用多进程编程。对于IO操作，使用多线程编程。
#操作系统切换线程要比进程开销小
#尽量使用多线程
#1.对于耗费cpu的操作，计算（图像，机器学习）。多进程>多线程
#2 对于IO操作来说，多线程>多进程
import time

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(5) as executor:
    all_task =[executor.submit(fib,(num)) for num in range(25,35)]
    start_time = time.time()
    for future in as_completed(all_task):
        data = future.result()
        print('exe result:{}'.format(data))

    print('last time:{}'.format(time.time()-start_time))


if __name__ == '__main__':
    from concurrent.futures import ProcessPoolExecutor,as_completed
    with ProcessPoolExecutor(4) as executor:
        all_task=[executor.submit(fib,(num)) for num in range(25,35)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print('exe result:{}'.format(data))

        print('last time:{}'.format(time.time() - start_time))