import socket
class DUMMY :

    type = 0x1000

    @staticmethod
    def intercept(client_socket: socket.socket, buffer: bytes) -> None :
        print("Pacote dummy interceptado")