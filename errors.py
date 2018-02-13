import socket
import argparse
import sys

def try_errors():
    #Getting the arguments parser ready
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', type=int, action='store', dest='port', required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)
    args = parser.parse_args()
    host = 'www.google.ro'
    port = 80
    file = 'errors.py'

    #1st Error
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Error creating socket: {}'.format(e))
        sys.exit(1)

    #2nd Error
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print('Address related connection error: {}'.format(e))
        sys.exit(1)
    except socket.error as e:
        print('Connection error: '.format(e))
        sys.exit(1)

    # #3rd Error
    # try:
    #     s.sendall('GET {} HTTP/1.0\r\n\r\n'.format(file))
    # except socket.error as e:
    #     print('Error sending data: {}'.format(e))
    #     sys.exit(1)

    #4th Error
    while True:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print('Error receiving data: {}'.format(e))
        if not len(buf):
            break
        sys.stdout.write(buf)

if __name__ == '__main__':
    try_errors()

