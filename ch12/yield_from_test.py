
from itertools import chain


my_list = [1,2,3]
my_dict = {
    'ss1':'qq.com',
    's2':'baidu.com'
}
#接受任意多个可传递对象
#yield from iterable
#yield 返回对象，yield from 返回里面的值

# for value in chain(my_list,my_dict):
#     print(value)

def my_chain(*args,**kwards):
    for my_iterable in args:
        for value in my_iterable:
            yield value

for value in my_chain(my_list,my_dict):
    print(value)

def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

#1.main调用方g1（委托生成器）gen子生成器
# yield from会在调用方与自生成器之间建立一个双向通道