import socket
def print_machine_info():
    host_name = socket.gethostname()
    ip_addres = socket.gethostbyname(host_name)
    print("Host name: %s" %host_name)
    print("Ip Address: %s" %ip_addres)
if __name__ == '__main__':
    print_machine_info()