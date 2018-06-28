

#生成器函数，函数里只要有yield关键字

def gen_fuc():
    yield 1
    yield 2

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1)+fib(index-2)

def fib2(index):

    pass


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1



def func():
    return 1

if __name__ == '__main__':
    #生成器函数返回的是生成器对象(python编译字节码的时候)
    gen = gen_fuc()
    re = func()

    for data in gen_fib(10):
        print(data)



    for value in gen:
        print(value)
    pass