import socket
from colorama import Fore

address = ('127.0.0.1', 1919)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

allowed_commands = ['OUT', 'ROMAN', 'INT']

is_connected = True
while is_connected:
    print(Fore.YELLOW + 'If you want to disconnect, type "out"' + Fore.RESET)
    command = input('Inform the type of the input ("roman" or "int"): ').replace(' ', '').upper()
    
    is_command_valid = command in allowed_commands
    
    if is_command_valid:
        if(command == 'OUT'):
            out_command = command + '| '
            client_socket.send(bytes(out_command, 'UTF-8'))
            server_response = client_socket.recv(2048)
            message = server_response.decode('utf-8')
            print(message)
            
            client_socket.close()
            print('You has been disconnected!')
            is_connected = False
        else:
            value = None
            if(command == 'ROMAN'):
                roman_string = input('Enter the roman number that you want to convert: ')
                value = roman_string.upper()
            elif(command == 'INT'):
                integer_to_be_converted = input('Enter the integer number that you want to convert: ')
                value = integer_to_be_converted

            payload_to_server = command + '|' + value
            client_socket.send(bytes(payload_to_server, 'UTF-8'))

            server_response = client_socket.recv(2048)
            message = server_response.decode('utf-8')
            print(message)
    else:
        print(Fore.RED + '\nInvalid command, please try again!\n' + Fore.RESET)
        continue

    