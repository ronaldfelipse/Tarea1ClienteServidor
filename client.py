#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import math

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8888")
print("Connecting to calculator server…")

#  Socket to talk to server


def Menu():
    print("Menu calculator\n1.Sum\n2.Substraction\n3.Multiplication\n4.Division\n5.Power\n6.Salir")

#  Do 10 requests, waiting each time for a response
def Calculator():
    while True:
        Menu()
        opc = input("Seleccione opción\n")
        if(opc=="6"):
            message = "{}".format(opc)
            socket.send_string(message)
            break
        else:
            x = input("Ingrese número\n")
            y = input("Ingrese otro número\n")
            message = "{}:{}:{}".format(opc,x,y)
            socket.send_string(message)
            message = socket.recv()
            print(message)

Calculator()




#for request in range(10):
#    s= str(request)
#    print("Sending request %s …" % request)
#    socket.send(s.encode("utf-8"))

#    print("Sending request %s …" % request)
#    socket.send((b"Hello"))
    #  Get the reply.
#    message = socket.recv()
    #print("Received reply %s [ %s ]" % (request, message))
#    print(request, message)
