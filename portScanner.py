#!/usr/bin/python3
import socket
ip = input("Enter the IP address: ")
port = int(input("Enter the port number: "))
# creates an INET, STREAMing socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sock.connect_ex((ip, port)):
    print("Port ", port, " is closed.")
else:
    print("Port ", port, " is open.")