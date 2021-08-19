import socket

address = ('127.0.0.1', 3333)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

while True:
    text = input('Type the message: ')

    client_socket.send(bytes(text, 'UTF-8'))

    if(text == 'out'):
        client_socket.close()
        break
    
    server_response = client_socket.recv(2048)
    message = server_response.decode('UTF-8')
    print(message)

    