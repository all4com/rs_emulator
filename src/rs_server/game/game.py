from common.network.TCPServer import TCPServer 
from common.network.PacketHandler import PacketHandler

import asyncio
import common.state as state

async def main():

    # Initialize packet handler
    handlers = PacketHandler()

    # Register handler functions 
    # no handlers at moment

    # Initialize server
    server = TCPServer("0.0.0.0", state.GAME_SERVER_PORT, handlers)

    await asyncio.gather(
        server.listen(),
        server.run_command_listener()
    )

if __name__ == "__main__" :
    asyncio.run(main())