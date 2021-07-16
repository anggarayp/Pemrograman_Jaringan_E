import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
# server = ('192.168.122.37', 10000) #alpine1
server = ('192.168.122.36', 10000) #alpine2
print(f"starting up on server {server}")
sock.bind(server)
# Listen for incoming connections
sock.listen(1)
while True: #selama ga keyboard interrupt
    # Wait for a connection
    print("waiting for a connection")
    connection, client = sock.accept() #nerima connection dr client
    print(f"connection from client {client}")
    # Receive the data in small chunks and retransmit it
    while True:
        data_pesan = connection.recv(1024) #server nerima pesan sbnyk 32 bytes
        print(f"menerima pesan {data_pesan}")
        if data_pesan:
            print("mengirim kembali pesan")
            connection.sendall(data_pesan)
        else:
            #print >>sys.stderr, 'no more data from', client_address
            #print(f"no more data from {client}")
            break
    # Clean up the connection
    connection.close()
