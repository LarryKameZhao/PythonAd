# 文件大概500g，只有一行

def myreadlines(f,newline):

    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos+len(newline):]

        chunk = f.read(4096*10)
        # 说明读到文件结尾
        if not chunk:
            yield buf
            break
        buf += chunk


if __name__ == '__main__':
    with open('index.txt') as f:
        for line in myreadlines(f,'#'):
            print(line)
