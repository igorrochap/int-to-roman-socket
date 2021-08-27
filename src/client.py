import socket
from colorama import Fore
from command import Command

address = ('127.0.0.1', 3333)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

command = Command()

is_connected = True
while is_connected:
    print(Fore.YELLOW + 'If you want to disconnect, type "out"' + Fore.RESET)
    text = input('Inform the type of the input ("roman" or "int"): ').lower()
    
    is_command_valid = command.verify_command(text)
    if is_command_valid:
        if(text == 'out'):
            out_command = 'out-out'
            client_socket.send(bytes(out_command, 'UTF-8'))
            client_socket.close()
            print('You has been disconnected!')
            is_connected = False
        else:
            if(text == 'roman'):
                roman_string = input('Enter the roman number that you want to convert: ')
                payload_to_server = text + '-' + roman_string.upper()
                client_socket.send(bytes(payload_to_server, 'UTF-8'))
                
            server_response = client_socket.recv(2048)
            message = server_response.decode('utf-8')
            print(message)
    else:
        print(Fore.RED + 'Invalid command, please try again!' + Fore.RESET)
        continue

    