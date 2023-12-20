### Simple UDP transeiver that prints the frame number and first 10 byte of data 

import socket
import struct

UPD_PORT = 4242
UDP_IP = '0.0.0.0' # Use '0.0.0.0' to bind to all available network interfaces


data_format = '1H 100B'  # define here the format used in the UDP client

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific port on the default IP address
udp_socket.bind((UDP_IP, UPD_PORT))  

print("UDP receiver is ready to receive data on port")
try:

    while True:
        data, address = udp_socket.recvfrom(10240)  # Receive data and the sender's address
        unpacked_data = struct.unpack(data_format, data)
        print(f"Received data from {address}: frame_number: {unpacked_data[0]}, data[1:10]: {unpacked_data[1:11]}  ")


except:
    # Close the socket when done (usually in a cleanup routine)
    udp_socket.close()  