import socket
import os
file_name = r"C:\Users\Admin\Desktop\cyber\yonatanSim\client_file"

host = '127.0.0.1'
port = 8080


s = socket.socket()

# התחברות לשרת
s.connect((host, port))
print("Connected to server")

def file_send():
    filename = input('Input full path of the file you want to send: ')
    
    try:
        with open(filename, "rb") as fi:
            data = fi.read(1024)
            while data:
                s.send(data)
                data = fi.read(1024)
        print("File sent successfully.")
    except IOError:
        print('You entered an invalid filename! Please enter a valid one.')

def file_recv(sock):
   data =  sock.recv(1024).decode()
   with open(file_name,"w")as file:
        if data:
            file.write(data)
file_send()

s.close()


