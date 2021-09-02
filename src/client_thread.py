import threading
from protocol import ConvertionProtocol
from colorama import Fore, Back, Style


class ClientThread(threading.Thread):
    def __init__(self, client, client_address):
        threading.Thread.__init__(self)
        self.client_socket = client
        self.client_address = client_address
    
    def run(self):
        protocol = ConvertionProtocol()
        print('New connection of:', Fore.YELLOW + '', self.client_address, '' + Fore.RESET)
        is_connected = True
        while is_connected:
            try:
                client_request = self.client_socket.recv(2048)
                client_request = client_request.decode('utf-8')

                command, to_convert = client_request.split('|')
                
                print(self.client_address, 'sent: [COMMAND = ' + command + ', OBJECT = ' + to_convert + ']')
                
                if (command != 'OUT'):
                    server_response = protocol.treat(command, to_convert)
                    self.client_socket.sendall(bytes(server_response, 'UTF-8'))
                else:
                    is_connected = False
                    disconnected_response = '\nSTATUS: 104\nMESSAGE: DISCONNECTED\n'
                    self.client_socket.sendall(bytes(disconnected_response, 'UTF-8'))
                    print(Fore.YELLOW + '', self.client_address, '' + Fore.RESET, 'has been disconnected')
            except Exception as e:
                print(e)
                error_message = '\nSTATUS: 101\nMESSAGE: INTERNAL ERROR\n'
                self.client_socket.sendall(bytes(error_message, 'UTF-8'))
