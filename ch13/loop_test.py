
import asyncio
import time
from functools import partial
async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')
    return 'SS'

def callback(future):
    print('send email to sss')

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    #get_future = asyncio.ensure_future(get_html('qq.com'))
    #tasks =[get_html('qq.com') for i in range(10)]
    #loop.run_until_complete(asyncio.wait(tasks))
    #loop.run_until_complete(get_future)
    task = loop.create_task(get_html('qq.com'))
    task.add_done_callback(callback)
    loop.run_until_complete(task)
    print(task.result())
    print(time.time()-start_time)