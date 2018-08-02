


def sales_sum(propname):
    total = 0
    nums = []
    while True:
        x = yield
        print(propname+':'+str(x))
        if not x:
            break;
        total += x
        nums.append(x)

    return total,nums


if __name__ == '__main__':
    my_gen= sales_sum('iphonte')
    my_gen.send(None)
    my_gen.send(1200)
    my_gen.send(3000)
    try:
        my_gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)
