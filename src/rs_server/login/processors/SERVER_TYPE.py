import asyncio
from common.helpers import print_binary
import common.state as state
from common.network.packets.regular import PACKET_SERVER_TYPE
from login.login_service import LoginService

class SERVER_TYPE :

    type = 0x1007

    @staticmethod
    async def intercept(client_socket: asyncio.StreamWriter, buffer: bytes) -> None :
        loginService = LoginService()
        server_list = state.server_model.find()
        for server in server_list:
            loginService.register_server(server["name"], server["type"])
        
        packet = PACKET_SERVER_TYPE.from_buffer_copy(buffer)
        buff = loginService.get_server_list_buffer()
        client_socket.write(loginService.get_server_list_buffer())
        await client_socket.drain()
