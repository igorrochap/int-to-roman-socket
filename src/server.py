import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, client, client_address):
        threading.Thread.__init__(self)
        self.client_socket = client
        self.client_address = client_address
    
    def run(self):
        print('New connection of:', self.client_address)
        while True:
            response = self.client_socket.recv(2048)
            response = response.decode('utf-8')
            if (response != 'out'):
                message = 'You send ' + response + ' to server'
                self.client_socket.sendall(bytes(message, 'UTF-8'))
            else:
                break        
        print(self.client_address, 'has been disconnected')
                

address = ('127.0.0.1', 3333)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
print('SERVER RUNNING')

while True:
    try:
        server_socket.listen(1)
        client, client_address = server_socket.accept()
        client_thread = ClientThread(client, client_address)
        client_thread.start() 
    except:
        break

server_socket.close()