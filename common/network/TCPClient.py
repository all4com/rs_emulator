import asyncio
from common.helpers import print_binary
from common.network.PacketHandler import PacketHandler
import common.state as state

class TCPClient:

    @staticmethod
    async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, handlers: PacketHandler) -> None:
        addr = writer.get_extra_info('peername')
        print(f"client on addr {addr} connected to the server.")
        
        client_port = addr[1]
        state.players[client_port] = {"writer": writer}

        try:
            while True:
                buffer = await reader.read(1024)
                if not buffer:
                    print(f"client on addr {addr} disconnected from the server.")
                    del state.players[client_port]
                    break

                await handlers.execute_packet(writer, buffer)  # Processar o pacote recebido

        except asyncio.CancelledError:
            print(f"client on addr {addr} forcefully disconnected.")
            del state.players[client_port]
        
        finally:
            writer.close()
            await writer.wait_closed()
