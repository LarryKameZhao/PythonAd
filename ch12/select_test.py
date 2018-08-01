import socket
from urllib.parse import urlparse
from selectors import DefaultSelector,EVENT_WRITE,EVENT_READ

selector = DefaultSelector
#selector http 请求s
class Fetcher:

    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send('GET {} HTTP/1.1\r\n\Host:{}\r\nConnection:close')
        selector.register(self.client.fileno(),EVENT_READ,)
    def get_url(self,url):
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == '':
            self.path = '/'
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host,80))
        except BlockingIOError  as e:
            pass



        selector.register(self.client.fileno(),EVENT_WRITE,)


def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path=='':
        path='/'
    #建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client.connect((host, 80))
            break
        except OSError as e:
            pass

    client.send('GET {} HTTP/1.1\r\n\Host:{}\r\nConnection:close'.format(path,host).encode('utf8'))

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode('utf8')
    print(data)
    print('success')
    client.close()


if __name__ == '__main__':
    get_url('http://www.baidu.com')