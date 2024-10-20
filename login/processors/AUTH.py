import socket
from common.security.crypto import CryptoUtils
from common.helpers import print_binary
from login.structs import CL_LOGIN


class AUTH :

    type = 0x1001

    @staticmethod
    def intercept(client_socket: socket.socket, buffer: bytes) -> None :
        crypt = CryptoUtils(buffer)
        buffer = crypt.decrypt()
        buffer : CL_LOGIN = CL_LOGIN.from_buffer_copy(buffer)

        print(buffer.username)
        xpto = crypt.decode_login_string(buffer.security_code_1, buffer.username)
        xpto = xpto.decode("Shift-JIS", "ignore")
        print(xpto)
