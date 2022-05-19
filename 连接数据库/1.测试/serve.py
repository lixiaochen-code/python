# coding = utf-8
from socket import *
from threading import Thread
import re  # 用正则表达式检索客户端的请求信息


def recvsocket(client_socket):
    recvdata = client_socket.recv(1024)
    print("request data:", recvdata)
    recv_lines = recvdata.splitlines()  # 将客户端请求的信息根据空格分割开
    for line in recv_lines:
        print(line)   # 打不打印都没关系，打印可以看到详细的内容
    request_start_line = recv_lines[0]  # 取第一行内容，是客户端的GET请求信息
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
    if "/" == file_name:  # 拿到请求的详细地址，如果是根目录，就将文件地址加上
        file_name = "/index.html"
    try:
        file = open(HTML_ROOT_DIR + file_name, "rb")  # 打开文件
    except IOError:  # 如果打不开，就返回文件不存在
        response_start_line = "HTTP/1.1 404 Not Found\r\n"  # 状态码
        response_headers = "Server: pycharm server\r\n"  # 响应头
        response_boby = "The file is not fund!"  # 响应码
    else:
        file_data = file.read()  # 能打开，就读取
        file.close()  # 关闭文件
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: pycharm server\r\n"
        response_boby = file_data.decode("utf-8")  # 响应报头，内容就是刚才读取的html文件
    response = response_start_line + response_headers + "\r\n" + response_boby
    print("response data:", response)
    client_socket.send(response.encode("utf-8"))
    client_socket.close()


if __name__ == '__main__':
    HTML_ROOT_DIR = "./html"  # 本地已经建好的html文件地址
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("", 12345))
    server.listen(5)
    while True:
        client_socket, ip_port = server.accept()
        print("%s:%s>>>正在连接中。。。" % ip_port)
        childthread = Thread(target=recvsocket, args=(client_socket,))
        childthread.start()
