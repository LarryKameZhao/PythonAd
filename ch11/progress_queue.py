
from multiprocessing import Process,Queue,Pipe
from multiprocessing import Manager
import time
queue = Queue(10)
#多进程不能用Queue，使用multiprocess.Queue.不能共享全局变量（多线程中可用)
#多进程是隔离的，会将变量副本传给另一个进程
#pool中的进程间通信需要使用Manager().Queue
# def producer(a):
#     a += 1
#     time.sleep(2)
#
# def consumer(a):
#     time.sleep(2)
#     print(a)


def producer(pipe):
    pipe.send('sss')


def consumer(pipe):
    time.sleep(2)
    print(pipe.recv())
if __name__ == '__main__':
    a = 1
    # queue = Manager().Queue(10)
    # my_producer = Process(target=producer,args=(a,))
    # my_consumer = Process(target=consumer,args=(a,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    #通过Pipe实现进程间通信
    #pipe只能适用于两个指定进程,pipe性能高于Queue



    receive_pipe,send_pipe =Pipe()
    my_producer = Process(target=producer, args=(receive_pipe,))
    my_consumer = Process(target=consumer,args=(send_pipe,))

    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()