import socket
import argparse

def echo_server(port):
    host = '127.0.0.1'
    data_payload = 2048
    backlog = 5
    #Facem un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Il setam in asa fel incat sa il putem utiliza de mai multe ori pe acelasi port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Facem legatura
    server_address = (host, port)
    print('Starting up echo server at {}'.format(server_address))
    s.bind(server_address)
    #Ascultam conectiunile
    s.listen(backlog)

    while True:
        print('Waiting for data: ')
        client, address = s.accept()
        data = client.recv(data_payload)
        if data:
            print('Data: {}'.format(data))
            client.send(data)
            print('Sending {} bytes to address {}'.format(data, address))
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    args = parser.parse_args()
    port = args.port
    echo_server(port)