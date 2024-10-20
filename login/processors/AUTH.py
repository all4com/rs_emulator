import asyncio
import common.state as state
from common.security.crypto import CryptoUtils
from common.helpers import print_binary
from login.structs import CL_LOGIN

class AUTH :

    type = 0x1001

    @staticmethod
    async def intercept(client_socket: asyncio.StreamWriter, buffer: bytes) -> None :

        # decrypt packet
        crypt = CryptoUtils(buffer)
        buffer = crypt.decrypt()

        # convert packet to a structured class
        buffer : CL_LOGIN = CL_LOGIN.from_buffer_copy(buffer)

        # decrypt credentials
        buffer.username = crypt.decode_login_string(buffer.security_code_1, buffer.username)
        buffer.password = crypt.decode_login_string(buffer.security_code_2, buffer.password)

        # create a user for tests
        if buffer.username.decode("utf-8").startswith("create_") :
            username = buffer.username.decode("utf-8").split("create_").pop()
            state.user_model.insert({"username": username, "password": buffer.password.decode("utf-8")})
            print(username)

             # search user from database
        result = state.user_model.getByUsername(buffer.username.decode("utf-8"))
        print(result)
