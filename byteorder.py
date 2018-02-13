import socket

def convert_byte():
    data = int(input('Enter some data: '))
    hton_long = socket.htonl(data)
    hton_short = socket.htons(data)
    ntoh_long = socket.ntohl(data)
    ntoh_short = socket.ntohs(data)
    print('Original: {} => Long host byte order = {}, Network byte order = {}'.format(data, ntoh_long, hton_long))
    print('Original: {} => Short host byte order = {}, Network byte order = {}'.format(data, ntoh_short, hton_short))

if __name__ == '__main__':
    convert_byte()
