import socket
def socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Default timeout is: {}'.format(s.gettimeout()))
    s.settimeout(100)
    print('Current timeout is: {}'.format(s.gettimeout()))

if __name__ == '__main__':
    socket_timeout()