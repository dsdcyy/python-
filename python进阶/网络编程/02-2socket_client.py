import socket
# 生成客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
client.connect(('127.0.0.1', 18888))
# 给服务器发送数据
while True:
    cil_data = ''
    if cil_data != '0':
        cil_data = input('>>>>')
        client.send('Client:{}'.format(cil_data).encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))
    else:
        client.close()
        break
    # client.close()
