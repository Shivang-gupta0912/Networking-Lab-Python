import socket
from threading import Thread
import os

class Client:

    def __init__(self, Host, Port):
        self.socket = socket.socket()
        self.name = input("Enter Your Name: ")
        self.socket.connect((Host, Port))
        
    def talk_to_server(self):
        self.socket.send(self.name.encode())
        print(f'Connected to server as {self.name}')
        Thread(target = self.receive_messages).start()
        self.send_messages()

    def receive_messages(self):
        while True:
            message = self.socket.recv(1024).decode()
            if not message.strip():
                print("Disconnected from server.")
                os._exit(0)
            else:
                print("\033[1;32m" + message + "\033[0m")  # Print message in green color]")
    
    def send_messages(self):
        while True:
            message = input()
            message = f'{self.name}: {message}'
            self.socket.send(message.encode())

if __name__ == "__main__":
    client = Client('localhost', 9999)
    client.talk_to_server()