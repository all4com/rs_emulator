import asyncio
from common.helpers import print_binary
from common.network.TCPClient import TCPClient
from common.network.PacketHandler import PacketHandler

class TCPServer :

    def __init__(self, HOST: str, PORT: int, handlers: PacketHandler) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.handlers = handlers
        self.stop_event = asyncio.Event()
        self.max_clients = 100
        self.clients = {}
        self.listen()

    async def handler_server(self, reader, writer) -> None:
        addr = writer.get_extra_info('peername')
        client_port = addr[1]
        try:
            self.clients[client_port] = writer
            await TCPClient.handler(reader, writer, self.handlers)
        except Exception as e:
            print(f"Error on client {addr}: {e}")
        finally:
            writer.close()
            await writer.wait_closed()

    async def listen(self) -> None:

        server = await asyncio.start_server(self.handler_server, self.HOST, self.PORT)
        print(f"Running server at {self.HOST}:{self.PORT}")

        async with server:
            await self.stop_event.wait()
            server.close()
            await server.wait_closed()

    async def run_command_listener(self):
        while True:
            command = await asyncio.get_event_loop().run_in_executor(None, input, "Write a command: ")
            if command == "exit":
                for port, writer in self.clients.items():
                    writer.close()
                    await writer.wait_closed()
                self.stop_event.set()
                break
 
            