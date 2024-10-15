# TODO: start using asyncio instead of threading

import threading
import socket
from common.helpers import print_binary
from common.network.TCPClient import TCPClient
from common.network.PacketHandler import PacketHandler
import subprocess

class TCPServer :

    def __init__(self, HOST: str, PORT: int, handlers: PacketHandler) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.stop_event = threading.Event()
        self.max_clients = 100
        self.handlers = handlers
        self.listen()

    def handler_server(self) -> None:
        self.server.listen()
        while not self.stop_event.is_set():
            try:
                # here we need to create a connection limit
                connection, addr = self.server.accept()
                client_thread = threading.Thread(
                    target=TCPClient.handler, args=(connection, addr, self.handlers)
                )
                client_thread.start()
            except socket.timeout:
                continue
            except OSError:
                break

    def listen(self) -> None:

        server_thread = threading.Thread(target=self.handler_server)
        server_thread.start()

        while True :
            command = input("Write a command: ")
            if command == "exit" :
                self.stop_event.set()
                self.server.close()
                break;
        
        print("Server stop listening...")
        server_thread.join()

            