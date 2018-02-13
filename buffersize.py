import socket

def set_buff_size():
    SEND_BUFF_SIZE = 4096
    RECV_BUFF_SIZE = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print('Actual buffer size is: {}'.format(bufsize))
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print('Modified buffer size is: {}'.format(bufsize))

if __name__ == '__main__':
    set_buff_size()