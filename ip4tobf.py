import socket
from binascii import hexlify
def ip4_to_binary():
    for ip_addres in ['127.0.0.1', '192.168.0.10']:
        packed_ip = socket.inet_aton(ip_addres)
        unpacked_ip = socket.inet_ntoa(packed_ip)
        print('IP Address: %s => Unpacked: %s, Packed: %s' %(ip_addres, hexlify(packed_ip), unpacked_ip))
if __name__ == '__main__':
    ip4_to_binary()