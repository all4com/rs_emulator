import socket
from common.helpers import print_binary
from common.network.PacketHandler import PacketHandler

class TCPClient :

    @staticmethod
    def handler(connection: socket.socket, addr, handlers: PacketHandler) -> None:
        with connection :
            print(f"client on addr {addr} connected to the server.")
            while True :
                buffer = connection.recv(1024)
                if not buffer:
                    print(f"client on addr {addr} disconnected from the server.")
                    break
                handlers.execute_packet(buffer)