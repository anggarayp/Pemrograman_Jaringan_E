import socket


SERVER_IP = '192.168.122.9' #server alpine 2
# SERVER_IP = '192.168.122.14' #server alpine 3
# SERVER_IP = '192.168.122.151' #server alpine 4
# SERVER_IP = '192.168.122.248' #server alpine 5
SERVER_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

sock.bind(("", SERVER_PORT))



while True:
    data, addr = sock.recvfrom(1024)
    #buffer size 1024
    print(addr)
    print("diterima ", data)
    print("dikirim oleh " , addr)