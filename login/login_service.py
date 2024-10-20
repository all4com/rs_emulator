from login.structs import SERVER_LIST, SERVER_INFO, MAX_NUMBER_OF_SERVERS
from ctypes import byref, string_at, sizeof

class LoginService :

    def __init__(self) -> None:
        self.server_packet = SERVER_LIST()
        self.server_list = []

    def get_server_list_buffer(self) -> bytes :
        self.server_packet.number_of_servers = len(self.server_list)
        server_info_array = (SERVER_INFO * MAX_NUMBER_OF_SERVERS)()
        for i, server in enumerate(self.server_list):
            server_info_array[i] = server
        self.server_packet.list_of_servers = server_info_array

        self.server_packet.packet_length = sizeof(SERVER_LIST)
        self.server_packet.packet_serial = 0
        return string_at(byref(self.server_packet), sizeof(SERVER_LIST))

    def register_server(self, name: str, type: int) -> None :
        server = SERVER_INFO()
        server.server_name = name.encode("utf-8")
        server.server_index = len(self.server_list)
        server.server_type = type
        self.server_list.append(server)

    