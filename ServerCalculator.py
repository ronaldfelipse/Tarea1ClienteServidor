import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8888")

while True:
    message = socket.recv()
    message = message.decode("utf-8")
    if(message=="6"):
        break
    values = message.split(":")
    if(values[0]=="1"):
        result = int(values[1]) + int(values[2])
    if(values[0]=="2"):
        result = int(values[1]) - int(values[2])
    if(values[0]=="3"):
        result = int(values[1]) * int(values[2])
    if(values[0]=="4"):
        result = int(values[1]) / int(values[2])
    if(values[0]=="5"):
        result = int(values[1]) ** int(values[2])
    print ("Recibí %s, El resultado es %s"%(message, result))
    #Se envía el resultado al cliente
    socket.send_string(str(result))
