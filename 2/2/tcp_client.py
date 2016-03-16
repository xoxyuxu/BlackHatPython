# -*- coding: utf-8 -*-
import socket

target_host = "www.google.co.jp"
target_port = 80

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect( (target_host, target_port))

# Transmit data
client.send("GET / HTTP/1.1\r\nHost: google.co.jp\r\n\r\n")

# Receive data
response = client.recv( 4096 )

print response

