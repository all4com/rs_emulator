import socket
from common.helpers import print_binary
from common.network.PacketHandler import PacketHandler
import common.state as state

class TCPClient :

    @staticmethod
    def handler(socket: socket.socket, addr, handlers: PacketHandler) -> None:
        with socket :
            print(f"client on addr {addr} connected to the server.")
            client_port = addr[1]
            state.players[client_port] = {"socket": socket}
            while True :
                buffer = socket.recv(1024)
                if not buffer:
                    print(f"client on addr {addr} disconnected from the server.")
                    del state.players[client_port]
                    break
                handlers.execute_packet(socket, buffer)