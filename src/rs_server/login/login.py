from common.network.TCPServer import TCPServer 
from common.network.PacketHandler import PacketHandler

from login.processors.DUMMY import DUMMY
from login.processors.SERVER_TYPE import SERVER_TYPE
from login.processors.AUTH import AUTH
from login.processors.CREATE_AVATAR_HANLDER import CREATE_AVATAR_HANLDER

import asyncio
import common.state as state

async def main():

    # Initialize packet handler
    handlers = PacketHandler()

    # Register handler functions 
    handlers.register_handler(DUMMY.type, DUMMY.intercept)
    handlers.register_handler(SERVER_TYPE.type, SERVER_TYPE.intercept)
    handlers.register_handler(AUTH.type, AUTH.intercept)
    handlers.register_handler(CREATE_AVATAR_HANLDER.type, CREATE_AVATAR_HANLDER.intercept)

    # Initialize server
    server = TCPServer("0.0.0.0", state.LOGIN_SERVER_PORT, handlers)

    await asyncio.gather(
        server.listen(),
        server.run_command_listener()
    )

if __name__ == "__main__" :
    asyncio.run(main())