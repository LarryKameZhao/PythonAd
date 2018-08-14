import asyncio

def callback(sleep_times):
    print('sleep {}s success'.format(sleep_times))

def stop_loop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_soon(callback,2)
    #now = loop.time()
    loop.call_soon(stop_loop,loop)
    #loop.call_later(1,callback,4)
    #loop.call_at
    loop.run_forever()