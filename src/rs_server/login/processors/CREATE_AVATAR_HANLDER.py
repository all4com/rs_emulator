import asyncio
from login.structs import CREATE_AVATAR
from common.security.crypto import CryptoUtils
from common.helpers import print_binary
from ctypes import sizeof
from common.network.packets.regular import JOB_NAME
class CREATE_AVATAR_HANLDER :

    type = 0x1004

    @staticmethod
    async def intercept(client_socket: asyncio.StreamWriter, buffer: bytes) -> None :

        crypt = CryptoUtils(buffer)
        decrypted_buffer = crypt.decrypt()
        packet = CREATE_AVATAR.from_buffer_copy(decrypted_buffer)

        print("NAME", packet.strName)
        print("JOB", JOB_NAME[packet.wJob])

        # CREATE THE LOGIC TO CREATE A AVATAR IN THE DATABASE
        
