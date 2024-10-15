import socket
import common.state as state
from common.network.packets.login_packets import PACKET_SERVER_TYPE

class SERVER_TYPE :

    type = 0x1007

    @staticmethod
    def intercept(client_socket: socket.socket, buffer: bytes) -> None :
        packet = PACKET_SERVER_TYPE.from_buffer_copy(buffer)

        print(state.players)
        print(f"Server type is {packet.server_type}")