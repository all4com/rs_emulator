import asyncio
import websockets
from common.helpers import print_binary
from common.network.TCPClient import TCPClient
from common.network.PacketHandler import PacketHandler
import common.state as state

class TCPServer :

    def __init__(self, HOST: str, PORT: int, handlers: PacketHandler) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.handlers = handlers
        self.stop_event = asyncio.Event()
        self.max_clients = 100
        self.clients = {}

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

    async def command_server(self, websocket, path):
        print(state.SERVER_NAME)
        async for command in websocket:
            response = f"[{state.SERVER_NAME}]ng: '{command}' is not found"
            if command == "exit":
                # print("exit!")
                for ws in self.clients.values():
                    await ws.close()
                self.stop_event.set()
                response = f"[{state.SERVER_NAME}]'{command}' executed: ok"
            await websocket.send(response)

    async def run_command_listener(self):
        server = await websockets.serve(self.command_server, "0.0.0.0", 8765)
        print("WebSocket server started on port 8765")

        await self.stop_event.wait()
        server.close()
        await server.wait_closed()
            