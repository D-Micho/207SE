import socket

#creating socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM).

#binding the address and port that client will connect to
s.bind(('127.0.0.1', 3423))

#how many connections we can make at the same time
s.listen(5)


def testing(inputs):

    #split up the user input
    inputs = inputs.split(' ')
    #numbers to be used and final numbers go in here
    result = []
    #Operations are stored in here until they are executed
    Operations = []
    while len(inputs) > 0:
        #if we can float() it means it is an integer and we can move it to the result list
        try:
            float(inputs[0])
            result.append(int(inputs[0]))
            inputs.pop(0)
        #otherwise we check which operation it is and store it then execute
        except ValueError:
            if inputs[0] == '+':
                result[0] = result[0] + result[1]
                result.pop(1)
                inputs.pop(0)
            elif inputs[0] == '-':
                result[0] = result[0] - result[1]
                result.pop(1)
                inputs.pop(0)
            elif inputs[0] == '/':
                result[0] = result[0] / result[1]
                result.pop(1)
                inputs.pop(0)
            elif inputs[0] == '*':
                result[0] = result[0] * result[1]
                result.pop(1)
                inputs.pop(0)
    else:
        return result[0]




while True:
    #make socket object for specific connection
    clientsocket, address = s.accept()
    #Let us know we made connection
    print("Connection from {address} has been established")
    #receive RPN data from client
    rcvdData = clientsocket.recv(1024).decode()
    #create variable to store RPN result
    a = str(testing(rcvdData))
    #send RPN result back to client
    clientsocket.send(a.encode())
    
    
