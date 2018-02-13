import socket

def socket_block():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(('127.0.0.1', 0))

    server_address = s.getsockname()
    print('Server connected at socket: {}'.format(server_address))

    while True:
        s.listen(1)

if __name__ == '__main__':
    socket_block()