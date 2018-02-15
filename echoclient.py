import socket
import argparse
import sys

def echo_client(port):
    host = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print('Connecting {}'.format(server_address))
    s.connect(server_address)

    try:
        message = 'Test message. This will be echoed'
        print('Sending {}'.format(message))
        s.sendall(message)
        amount_received = 0
        amount_expected = len(message)
        if amount_received < amount_expected:
            data = s.recv(16)
            amount_received += len(data)
            print('Received: {}'.format(data))
    except socket.error as e:
        print('Socket error: {}'.format(e))
    except Exception as e:
        print('Other error: {}'.format(e))
    finally:
        s.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    args = parser.parse_args()
    port = args.port
    echo_client(port)

