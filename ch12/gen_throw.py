
def gen_func():
    try:
        yield 'hhhh'
    except Exception as e:
        pass
    yield 2
    yield 3

    return 'sss'


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception,'error')
    print(next(gen))
    gen.throw(Exception,'error2')