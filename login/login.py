from common.network.TCPServer import TCPServer 
from common.network.PacketHandler import PacketHandler

class Login :

    def __init__(self) -> None:

        handlers = PacketHandler()
        handlers.register_handler(0x1000, lambda _: print("Vishe maria"))
        server = TCPServer("127.0.0.1", 55661, handlers)

if __name__ == "__main__" :
    Login()