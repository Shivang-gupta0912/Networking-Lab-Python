import socket
from threading import Thread

class Server:
    Clients = []

    def __init__(self, HOST, PORT):
        self.socket = socket.socket()
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)
        print('Server started, waiting for connections...')

    def start_listen(self):
        while True:
            client_socket, addr = self.socket.accept()
            print(f'Connection from {addr} has been established.')

            client_name = client_socket.recv(1024).decode()
            self.broadcast(client_name, f'{client_name} has joined the chat.') # broadcast to be made

            client = {'client_socket' : client_socket, 'name' : client_name}
            Server.Clients.append(client)

            Thread(target = self.handle_client, args = (client,)).start()
    
    def handle_client(self, client):
        client_socket = client['client_socket']
        client_name = client['name']

        while True:
            message = client_socket.recv(1024).decode()
            if message.strip() == client_name + ': bye' or not message.strip():
                self.broadcast(client_name, f'{client_name} has left the chat!')
                client_socket.close()
                Server.Clients.remove(client)
                print(f'{client_name} has disconnected.')
                break
            else:
                self.broadcast(client_name, message)
    
    def broadcast(self, sender_name, message):
        for client in Server.Clients:
            client_name = client['name']
            client_socket = client['client_socket']

            if client_name != sender_name:
                client_socket.send(f'{message}'.encode())

if __name__ == "__main__":
    server = Server('localhost', 9999)
    server.start_listen()
