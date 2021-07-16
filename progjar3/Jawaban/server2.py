import socket

UDP_IP_ADDRESS = '192.168.122.31'
UDP_PORT = 88

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind(((UDP_IP_ADDRESS,UDP_PORT)))
filename='server1.jpg'
fp = open(filename,'wb+')
wrt=0
count=0
while True:
    data, addr = serverSock.recvfrom(1024)
    count=count+len(data)
    print(addr," block ", count,"long data : ",len(data), data)
    fp.write(data)