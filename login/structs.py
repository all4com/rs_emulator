from common.network.packets.regular import PACKET_BASE
from ctypes import LittleEndianStructure
from ctypes.wintypes import WORD, CHAR

MAX_NUMBER_OF_SERVERS = 20
WORLD_NAME_LENGTH = 32
AUTH_CREDENTIALS_LENGTH = 20
SELECTED_SERVER_LENGTH = 18

class SERVER_INFO(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("server_name", CHAR * WORLD_NAME_LENGTH),
        ("server_type", WORD, 10),
        ("is_local_open", WORD, 1),
        ("server_index", WORD),
        ("server_message_index", WORD), # this value is define at textData.dat, here is just the index
    ]
    def __init__(self) -> None:
        self.server_name = b''
        self.server_type = 0
        self.is_local_open = 0 
        self.server_index = 0 
        self.server_message_index = 0 

class SERVER_LIST(PACKET_BASE) :
    _pack_ = 1
    _fields_ = [
        ("number_of_servers", WORD),
        ("security_code", WORD),
        ("list_of_servers", SERVER_INFO * MAX_NUMBER_OF_SERVERS),
    ]
    def __init__(self) -> None:
        self.packet_type = 0x1102
        self.number_of_servers = 0
        self.security_code = 0
        self.list_of_servers = (SERVER_INFO * MAX_NUMBER_OF_SERVERS)()

class CL_LOGIN(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("client_version", WORD),
        ("username", CHAR * AUTH_CREDENTIALS_LENGTH),
        ("password", CHAR * AUTH_CREDENTIALS_LENGTH),
        ("selected_server_name", CHAR * SELECTED_SERVER_LENGTH),
        ("client_mac_address", CHAR * 64),
        ("client_code", CHAR * 12),
        ("b1IsYahoo", WORD, 1),
        ("b1IsDisconnectExistID", WORD, 1),
        ("b1IsUseToken", WORD, 1),
        ("security_code_1", WORD),
        ("security_code_2", WORD),
        ("token", CHAR * 64)
    ]
    def __init__(self) -> None:
        self.client_version = 0
        self.username = b''
        self.password = b''
        self.selected_server_name = b''
        self.client_mac_address = b''
        self.client_code = b''
        self.b1IsYahoo = 0
        self.b1IsDisconnectExistID = 0
        self.b1IsUseToken = 0
        self.security_code_1 = 0
        self.security_code_2 = 0
        self.token = b''