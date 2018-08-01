def gen_func():
    html = yield  "baidu.com"
    print(html)
    yield 2
    yield 3
    return 'sss'


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
