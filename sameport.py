import socket

def use_same_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    old_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print('Old state: {}'.format(old_state))

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print('New state: {}'.format(new_state))

    local_port = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)

    print('Listening on port: {}'.format(local_port))
    while True:
        try:
            connection, addr = srv.accept()
            print('Connected by {}:{}'.format(addr[0], addr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as e:
            print(e)

if __name__ == '__main__':
    use_same_port()