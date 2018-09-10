# pip install opcua

from opcua import Client
import time

url = "opc.tcp://192.168.1.6:4840"

client = Client(url)

client.connect()
print("Client Connected")

while True:
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print("\nTemperature: " + str(Temperature))

    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print("Pressure: " + str(Pressure))

    TIME = client.get_node("ns=2;i=4")
    TIME_Value = TIME.get_value()
    print("TIME_Value: " + str(TIME_Value))

    time.sleep(1)