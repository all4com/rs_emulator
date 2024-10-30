import asyncio
import common.state as state
from common.security.crypto import CryptoUtils
from common.helpers import print_binary
from login.structs import CL_LOGIN, RESULT_LOGIN, AVATAR_LIST
from ctypes import string_at, byref, sizeof
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
            state.user_model.insert({"username": username, "password": buffer.password.decode("utf-8"),"is_banned": 0, "banned_comment":"", "banned_data":""})
            print(username)

        input_username = buffer.username.decode("utf-8")
        input_password = buffer.password.decode("utf-8")

        # search user from database
        cond = {"username": input_username}
        result = state.user_model.select(conditions=cond)
        
        result_login = RESULT_LOGIN()

        if len(result) > 0 :

            db_username = result["username"]
            db_password = result["password"]
            db_is_banned = result["is_banned"]
            db_banned_comment = result["banned_comment"]
            db_banned_data = result["banned_data"]

            if db_is_banned == 1 :
                print(db_banned_comment, db_banned_data, db_is_banned)
                result_login.set_banned(int(db_banned_data), db_banned_comment)
                result_buffer = string_at(byref(result_login), sizeof(RESULT_LOGIN()))
                client_socket.write(result_buffer)
            else :
                if db_username == input_username and db_password == input_password :
                    result_login.set_success()
                    result_buffer = string_at(byref(result_login), sizeof(RESULT_LOGIN()))
                    client_socket.write(result_buffer)

                    # TODO: need to create table for avatars and apply the avatar logic here 
                    avatar_list = AVATAR_LIST()
                    avatar_list_buffer = string_at(byref(avatar_list), sizeof(AVATAR_LIST()))
                    client_socket.write(avatar_list_buffer)
                    
                    await client_socket.drain()

