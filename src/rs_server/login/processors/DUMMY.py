import asyncio

class DUMMY :

    type = 0x1000

    @staticmethod
    async def intercept(client_socket: asyncio.StreamWriter, buffer: bytes) -> None :
        pass