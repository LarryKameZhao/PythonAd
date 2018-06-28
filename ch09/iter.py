
#迭代协议
#迭代器是访问集合内元素的一种方式，一般用来遍历数据
#迭代器和下标的访问方式不一样，迭代器是不能返回的
#迭代器提供一种惰性访问方式
#[0]  使用的是迭代协议 __iter__方法，可迭代__iter__,迭代器需要__next__
#Iterable可迭代,  Iterator迭代器

from collections.abc import Iterable,Iterator


a= [1,2]

iter_rator = iter(a)
print(isinstance(iter_rator,Iterator))

print(isinstance(a,Iterable))

print(isinstance(a,Iterator))


