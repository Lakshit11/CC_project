import socket
import pandas as pd

PORT = 5050
SERVER = "xxx.xxx.xx.xxx" # ip address hidden for privacy and security reasons (Please contact owner of this repository to get IP address)
# SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def start():
    connection = connect()
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        #code to extract threadno
        start = msg.index(", ") + 2
        end = msg.index("]")
        number = int(msg[start:end-1])
        df = pd.read_csv('data.csv',header= 0)
        #code to get name associated with the threadno
        name = df[df['tno']==number]['Uname'].values[0]

        # printing message in the format of name: message
        msg1 = msg.split("]")[1].strip()
        print(name,":",msg1)

start()
