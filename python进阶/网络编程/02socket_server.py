import socket
import threading

# 生成服务器
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听绑定
server.bind(('0.0.0.0', 18888))
# 等待客户端连接
server.listen()


def handle_sock(sock, addr):
    # 获取从客户端发送的数据
    data = sock.recv(1024)
    # 将获得的数据解码
    print(data.decode('utf-8'))
    # 发送消息给客户端,数据encode加码
    ser_data = input('>>>>')
    sock.send('Server:{}'.format(ser_data).encode('utf-8'))


while True:
    # 接收用户连接请求，获得socker和address
    sock, addr = server.accept()
    # 实现多用户连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
