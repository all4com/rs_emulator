from common.network.packets.regular import PACKET_BASE
from common.helpers import int_to_little_endian_hex
import asyncio
class PacketHandler :

    handlers = {}

    def register_handler(self, id: int, method) -> None:
        if id not in self.handlers :
            self.handlers[id] = method

    async def execute_packet(self, client_socket: asyncio.StreamWriter, buffer: bytes) -> None:
        base = PACKET_BASE.from_buffer_copy(buffer)
        if base.packet_type in self.handlers :
            await self.handlers[base.packet_type](client_socket, buffer)
        else :
            print(f"Packet type {int_to_little_endian_hex(base.packet_type)} not implemented")