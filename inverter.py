import socket
from data import *

connections = []


def start_modbus():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('', 502)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        global connections
        connection, address = sock.accept()
        print('connection from', address)
        connections.append(connection)


def update():
    updated = False
    for connection in connections:
        try:
            connection.send(bytearray.fromhex(
                "5CF20001000AFF045150494753B7A90D"))
            data = connection.recv(128)

            LastData.Input_AC_Voltage = data[9:14]
            LastData.Input_AC_Frequency = data[15:19]
            LastData.Output_AC_Voltage = data[20:25]
            LastData.Output_AC_Frequency = data[26:30]
            LastData.Load_In_Watt = data[36:40]
            LastData.Battery_Voltage = data[49:54]
            LastData.PV_Input_Voltage = data[73:78]
            LastData.PV_Input_Watt = data[106:111]
            updated = True
        except:
            # Clean up the connection
            connection.close()
            connections.remove(connection)
            print("Connection closed: ", connection)
    return updated
