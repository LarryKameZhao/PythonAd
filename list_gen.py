
odd_list = []

for i in range(21):
    if i%2==1:
        odd_list.append(i)


def handle_item(item):
    return item+2

odd_list = [handle_item(i) for i in range(21) if i%2 ==1]
print(odd_list)


#生成器表达式
odd_gen = (i for i in range(21) if i%2==0)
print(type(odd_gen))
print(odd_gen)
# for item in odd_gen:
#     print(item)


#字典推倒
my_dict = {'bobby':22,'jack':24,'imooc.com':5}

reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)

#集合推倒
my_set = {'name:'+key for key,value in my_dict.items()}
print(type(my_set))
print(my_set)

