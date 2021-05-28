import sys
import socket

# Create a TCP/IP socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server1 = ('192.168.122.249', 10000)
server2 = ('192.168.122.91', 10000)
print(f"connecting to {server1}")
print(f"connecting to {server2}")
sock1.connect(server1)
sock2.connect(server2)

try:
    # Send data image
    pesan = open("nikizefanya_69376823_432745240665038_9036714333603567775_n.jpg", 'rb')
    baca_pesan = pesan.read()
    print(f"mengirim pesan {pesan}")
    sock1.sendall(baca_pesan)
    sock2.sendall(baca_pesan)

    # Look for the response alpine 1
    amount_received1 = 0
    amount_expected1 = len(baca_pesan)
    file1 = bytearray()
    while amount_received1 < amount_expected1:
        data_img1 = sock1.recv(16)
        amount_received1 += len(data_img1)
        file1 += data_img1
        print("data dikirim alpine 1: ", f"{data_img1}")
    
    # write file respon dari alpine 1
    write1 = open("niki_alpine1.jpg", 'wb')
    write1.write(file1)
    write1.close()

    # Look for the response alpine 2
    amount_received2 = 0
    amount_expected2 = len(baca_pesan)
    file2 = bytearray()
    while amount_received2 < amount_expected2:
        data_img2 = sock2.recv(16)
        amount_received2 += len(data_img2)
        file2 += data_img2
        print("data dikirim dari alpine2: ", f"{data_img2}")

    # write file respon dari alpine 2
    write2 = open("niki_alpine2.jpg", 'wb')
    write2.write(file2)
    write2.close()

finally:
    print("closing")
    sock1.close()
    sock2.close()