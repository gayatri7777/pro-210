import socket
from  threading import Thread
import time
import os


IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")
    
    global PORT
    global IP_ADDRESS
    global SERVER
    
    SERVER = socket.secket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    
    SERVER.listen(100)
    
    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")
    
def acceptConnections():
    global SERVER
    global client
    
    
    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096),decode().lower()
        clients[client_name] = {
            "client"    : client,
            "address"   : addr,
            "connected_with" : "",
            "file_name"      : "",
            "file_size"      : 4096
        }
            
        print(f"Connection established with {client_name} : {addr}")
        
        thread = Thread(target = handleClient, args = (client,client_name,))
        thread.start()
        
        
        
        
def setup():
    print("\n\t\t\t\t\t\tIP_MESSENGER\n")
    
    global PORT
    global IP_ADDRESS
    global SERVER
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    
    SERVER.listen(100)
    
    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")
    
    acceptConnections()
    
setup_thread = Thread(target=setup)
setup_thread.start()
    
