import socket
file_name = r"C:\Users\Admin\Desktop\cyber\yonatanSim\server_files"
def file_get(sock):
    filename = input('Input filename you want to send: ')
    try:
        with open(filename, "r") as fi:
            data = fi.read()
            if data:
                sock.send(data.encode())
            else:
                print("File is empty.")
    except IOError:
        print('You entered an invalid filename! Please enter a valid name')
def file_recv(sock):
   data =  sock.recv(1024).decode()
   with open(file_name,"w")as file:
        if data:
            file.write(data)
            
    
s = socket.socket()
print("Socket successfully created")
port = 8080
s.bind(('127.0.0.1', port))
print("Socket binded to %s" % (port))
s.listen(1)
print("Socket is listening")
c, addr = s.accept()
print('Got connection from', addr)
file_get(c)
file_recv(c)
c.close()
