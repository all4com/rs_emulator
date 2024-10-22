from common.network.TCPServer import TCPServer 
from common.network.PacketHandler import PacketHandler
from dotenv import load_dotenv

import asyncio
import os

async def main():

    #load environment
    load_dotenv()
    server_port = os.getenv("GAME_SERVER_PORT") 

    # Initialize packet handler
    handlers = PacketHandler()

    # Register handler functions 
    # no handlers at moment

    # Initialize server
    server = TCPServer("0.0.0.0", server_port, handlers)

    await asyncio.gather(
        server.listen(),
        server.run_command_listener()
    )

if __name__ == "__main__" :
    asyncio.run(main())