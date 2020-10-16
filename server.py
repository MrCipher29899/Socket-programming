import sys
import os
import socket

#create socket ( to allow 2 computer to connect)
''' 
link https://www.geeksforgeeks.org/socket-programming-python/'''

def socket_create():
    try:
        global host
        global port
        global s
        host=""
        port=9999
        s = socket.socket()
    except socket.error as msg:
        print("socket error "+str(msg))


def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port"+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("socket error "+str(msg)+"\n"+"Replying")
        socket_bind()

def socket_accept():
    conn,addr = s.accept()
    print("connection has established|"+"IP "+addr[0]+"|Port "+str(addr[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end="")

    

socket_create()
    
socket_bind()
socket_accept()
#This program is ended








    

    



