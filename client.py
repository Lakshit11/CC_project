import socket
import time
import csv
import subprocess
import os


PORT = 5050
SERVER = "xxx.xxx.xx.xxx" # ip address hidden for privacy and security reasons (Please contact owner of this repository to get IP address)
# SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1. Provides intercommunication capability for sockets. 2. Specifies TCP IP Socket.
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def server_thread(client):
    g = b'get_threadno'
    client.send(g)
    tno = client.recv(1024).decode()
    start = tno.index(", ") + 2
    end = tno.index("]")
    number = int(tno[start:end-1]) 
    return number

def start():

    #csv code
    name = input("Enter your name: ")
    connection = connect()
    thread_no = connection.getsockname()[1]
    tno = server_thread(connection)

    subprocess.Popen(['cmd','/c','start','python','list_messages.py'],shell=True)
    # subprocess.Popen(['cmd','/c','start','python','messge_logs.py'],shell=True)
    with open('data.csv','a+',newline = "") as f:
        writer = csv.writer(f)
        writer.writerow([thread_no,tno,name])
    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            # Exiting the terminal
            os.system('exit')

            #truncating the names file after exit
            with open('data.csv', 'r') as in_file:
                reader = csv.reader(in_file)
                header = next(reader)
                with open('data.csv', 'w', newline='') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerow(header)
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')

start()
