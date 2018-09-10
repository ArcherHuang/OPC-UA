# sudo pip install opcua

from opcua import Server
from random import randint
import datetime
import time
import receiveMSMQ

server = Server()

url = "opc.tcp://192.168.1.8:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)

Temp.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    
    Temperature = receiveMSMQ.get_from_msmq()
    print(Temperature)
    Temp.set_value(Temperature)
    time.sleep(2)