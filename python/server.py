#!/usr/bin/python2

import socket
import threading

host = ''
port = 18211

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))
sock.listen(5)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    if(request!=""):
        client_socket.send("whatsup?")
    print "Header: %s" % request

    data = ''
    data_len = 0

    while True:
        data = client_socket.recv(1024)
        print "recv: %s" % data
        data_len = len(data)
        data = ''
        if data_len < 1024:
            break

    client_socket.close()

while True:
    client,addr = sock.accept()

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
