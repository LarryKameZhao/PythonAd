#set是无序集合（不重复），frozenset是不可变集合
#set方法的difference是做和另一个set的差值
#s1.difference(s2) ==   s1-s2
#set支持   |&-

#issubset一个集合是否是另一个集合子集
s = set('123')
s1 = set('efg123')
s3 = set('e')
s1.update(s)
s2 = {'a','b'}
#frozenset用作dict的key
fs =frozenset([1,2,3,4,5])

if __name__=='__main__':
    print(s1.difference(s))
    print(s1&s)
    print(s1|s)
    if 'e' in s1:
        print('yes')

    print(s3.issubset(s1))
    print(type(s2))
    print(fs)
    print('------------------')