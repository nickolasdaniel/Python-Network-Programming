import socket
def remote_machine_info():
    host_name = socket.gethostname()
    try:
        remote_host = 'www.google.com'
        print('The IP Address of %s is: %s' %(remote_host, socket.gethostbyname(remote_host)))
    except socket.error as msgerror:
        print('%s : %s' %(remote_host, msgerror))
if __name__ == '__main__':
    remote_machine_info()