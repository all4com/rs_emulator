from common.network.packets.login_packets import PACKET_BASE
from common.helpers import int_to_little_endian_hex
import socket
class PacketHandler :

    handlers = {}

    def register_handler(self, id: int, method) -> None:
        if id not in self.handlers :
            self.handlers[id] = method

    def execute_packet(self, client_socket: socket.socket, buffer: bytes) -> None:
        base = PACKET_BASE.from_buffer_copy(buffer)
        if base.type in self.handlers :
            self.handlers[base.type](client_socket, buffer)
        else :
            print(f"Packet type {int_to_little_endian_hex(base.type)} not implemented")