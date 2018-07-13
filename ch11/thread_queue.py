import time
import threading

detail_url_list = []

def get_detail_html(detail_url_list):
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print('get_detail html started')
            time.sleep(2)
            print('get detail html end')

def get_detail_url(detail_url_list):
    while True:
        print('get_detail url start')
        time.sleep(4)
        for i in range(40):
            detail_url_list.append('id:'+str(i))
        print('get detial url end')

#线程间的通信方式-1共享变量
if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url,args=(detail_url_list))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html,args=(detail_url_list))
        html_thread.start()

    start_time = time.time()
