
#通过queue的方式进行线程间同步
import threading
from queue import Queue
from time import time
detail_url_list = []

def get_detail_html(queue):
    while True:
        url = queue.get()
        print('get_detail html started')
        time.sleep(2)
        print('get detail html end')

def get_detail_url(queue):
    while True:
        print('get_detail url start')
        time.sleep(4)
        for i in range(40):
            queue.put('id:'+str(i))
        print('get detial url end')


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url,args=(detail_url_queue))