#使用多线程：在协程中集成阻塞IO

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def get_url(url):
    return url
if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(3)
    start_time = time.time()
    tasks = []
    for url in range(20):
        url='qq.com'
        task = loop.run_in_executor(executor,get_url,url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print('last_time:{}'.format(time.time()-start_time))