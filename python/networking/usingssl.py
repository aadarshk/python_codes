#!/usr/bin/python3
import ssl
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssock = ssl.wrap_socket(sock)

try:
    ssock.connect(("www.google.com",443))
    print(ssock.cipher())
except:
    print("error")

try:
    ssock.write(b"GET / HTTP/1.1 \r\n")
    ssock.write(b"Host: www.google.com\n\n")
except Exception as e:
    print("write error",e)

data = bytearray()

try:
    data = ssock.read()
except Exception as e:
    print("read error")

print(data.decode("utf-8"))
