import sys
import socket
import string
import random

# Create a TCP/IP socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #bikin socket/kabel
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server1 = ('192.168.122.37', 10000) #bikin ip sm port alphine1
server2 = ('192.168.122.36', 10000) #alphine2
print(f"connecting to {server1}")
print(f"connecting to {server2}")
sock1.connect(server1) #trus diconnect ke server
sock2.connect(server2)

try:
    # Send data
    pesan = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000000))
    print(f"mengirim pesan {pesan}")
    sock1.sendall(pesan.encode()) #client ngirim pesan ke server
    # Look for the response
    amount_received = 0
    amount_expected = len(pesan)
    while amount_received < amount_expected:
        data_pesan = sock1.recv(512) #nerima data dari server, cuma 16 bytes
        amount_received += len(data_pesan)
        print(f"{data_pesan}")

    pesan2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000000))
    print(f"mengirim pesan {pesan2}")
    sock2.sendall(pesan2.encode()) #client ngirim pesan ke server
    # Look for the response
    amount_received2 = 0
    amount_expected2 = len(pesan2)
    while amount_received2 < amount_expected2:
        data_pesan2 = sock2.recv(512) #menerima data dari server, cuma 16 bytes
        amount_received2 += len(data_pesan2)
        print(f"{data_pesan2}")
finally:
    print("closing")
    sock1.close()
    sock2.close()