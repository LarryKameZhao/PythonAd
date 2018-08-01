
def gen_func():
    #1.可以产出值2.可以接收值（调用方法传递进来的值）
    yield 1
    name = yield "name1"
    print(name)
    yield 2
    yield 3
    return 'sss'


"""
启动生成器：next()  ,send方法可以将值传递进入生成器内部，同时
还可以重启生成器执行到下一个
"""
if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    print(next(gen))
    name = 'zje'
    print(gen.send(name))
    # print(next(gen))
