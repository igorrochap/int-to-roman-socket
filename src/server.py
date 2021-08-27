import socket
from colorama import Fore
from client_thread import ClientThread


address = ('127.0.0.1', 3333)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
print(Fore.GREEN + 'Server running at:' + Fore.RESET, address[0] + ':' + str(address[1]))

while True:
    try:
        server_socket.listen(1)
        client, client_address = server_socket.accept()
        client_thread = ClientThread(client, client_address)
        client_thread.start() 
    except:
        break

server_socket.close()