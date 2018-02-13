import socket
def find_protocol():
    protocol ='tcp'
    for port in [80, 25]:
        print('Port: {} => service name: {}'.format(port, socket.getservbyport(port, protocol)))
    print('Port: {} => service name: {}'.format(22, socket.getservbyport(22, 'tcp')))

if __name__ == '__main__':
    find_protocol()