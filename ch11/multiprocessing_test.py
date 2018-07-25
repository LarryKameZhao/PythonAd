import os
import time

#fork只能用于linux/unix中
#pid = os.fork()

import multiprocessing

#多进程

import time
def get_html(n):
    time.sleep(n)
    #print('sub progress success')
    return n*n


if __name__ == '__main__':

    # progress = multiprocessing.Process(target=get_html,args=(2,))
    # progress.start()
    # progress.join()
    # print('main progress end')

    #使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html,args=(3,))
    #等待所有任务完成.使用join必须先close（）
    # pool.close()
    # pool.join()
    # print(result.get())
    #imap
    for result in  pool.imap(get_html,[1,5,3]):
        print('{}sleep success'.format(result))