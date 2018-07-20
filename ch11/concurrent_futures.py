from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import Future


#线程池
#主线程中可以获取某个线程的状态或者任务的状态以及返回值
#当一个线程完成的时候，我们主线程能立即知道返回值
#futures可以让多线程和多进程编码一致

import time

def get_html(times):
    time.sleep(times)
    print("get page{}s success".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=3)
#通过submit函数提交执行的函数到线程池，submit立即返回
task1 = executor.submit(get_html,(3))
task2 = executor.submit(get_html,(4))

task_list = [3,2,4]
all_tasks = [executor.submit(get_html(url) )for url in task_list]

for future in executor.map(get_html,all_tasks):
    data = future.result()
    print('get{} page success'.format(data))
#done方法用于判定某个任务是否完成
# print(task1.done())
# #result方法可以获取tastk的执行结果
# print(task1.result())
#
# print(task2.result())