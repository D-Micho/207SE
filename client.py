import socket

#create socket object
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server
s.connect(('127.0.0.1',3423))

while True:

    #Take RPN values
    num1 = raw_input("Enter RPN Values With Spaces")
    #Send RPN values
    s.send(num1.encode())
    #Receive RPN Result
    rcvdData = s.recv(1024).decode()
    #Print Result
    print(rcvdData)
    
