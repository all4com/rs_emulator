from common.network.packets.regular import PACKET_BASE
from common.helpers import int_to_little_endian_hex
import socket
class PacketHandler :

    handlers = {}

    def register_handler(self, id: int, method) -> None:
        if id not in self.handlers :
            self.handlers[id] = method

    def execute_packet(self, client_socket: socket.socket, buffer: bytes) -> None:
        base = PACKET_BASE.from_buffer_copy(buffer)
        if base.packet_type in self.handlers :
            self.handlers[base.packet_type](client_socket, buffer)
        else :
            print(f"Packet type {int_to_little_endian_hex(base.packet_type)} not implemented")