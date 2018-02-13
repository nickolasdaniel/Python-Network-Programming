import socket

def input_protocol():
    protocol = input('Enter a valid protocol: ')
    port = int(input('Enter a valid port: '))
    print('Service is: {}'.format(socket.getservbyport(port, protocol)))

if __name__ == '__main__':
    input_protocol()