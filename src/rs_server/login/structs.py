from typing import Any
from common.network.packets.regular import PACKET_BASE
from ctypes import LittleEndianStructure, sizeof
from ctypes.wintypes import WORD, CHAR, DWORD

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


RESULT_LOGIN_SUCCESS = 0x000
RESULT_LOGIN_FAILED = 0x001
RESULT_LOGIN_USEDID = 0x002
RESULT_LOGIN_RETRY = 0x003
RESULT_LOGIN_NOT_SAME_VERSION = 0x004
RESULT_LOGIN_OTP = 0x005
RESULT_LOGIN_SUCCESS_BUT_NOT_USE_OTP = 0x006
RESULT_LOGIN_SUCCESS_PERSONALCOM = 0x007
RESULT_LOGIN_FAIL_PERSONALCOM = 0x008

class RESULT_LOGIN(PACKET_BASE):
    _pack_ = 1
    _fields_ = [
        ("result_type", DWORD),
        ("client_code", DWORD),
        ("security_code", WORD),
        ("reason_of_ban", CHAR * 64)
    ]
    def __init__(self) -> None:
        self.packet_length = sizeof(RESULT_LOGIN)
        self.packet_type = 0x1101
        self.packet_serial = 0
        self.result_type = RESULT_LOGIN_FAILED
        self.security_code = 0
        self.client_code = 0

    def set_success(self):
        self.result_type = RESULT_LOGIN_SUCCESS

    def set_fail(self):
        self.result_type = RESULT_LOGIN_FAILED

    def set_banned(self, date: int, message: str):
        self.reason_of_ban = message.encode("utf-8")
        self.result_type = date


# 0x1103

MAX_AVATAR_COUNT = 6
NAME_LENGTH = 18

class AVATAR_INFO(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("m_strName", CHAR * NAME_LENGTH),
        ("m_wJob", WORD),
        ("m_wLevel", WORD),
        ("m_aEquip", WORD * 2 * 3),
        ("m_wLastVillage", WORD)
    ]

    def __init__(self) -> None:
        self.m_strName = b'noname'
        self.m_wJob = 0 * 2
        self.m_wLevel = 1
        for i in range(2):
            for j in range(3):
                self.m_aEquip[i][j] = 0xFFFF
        self.m_wLastVillage = 0

class AVATAR_LIST(PACKET_BASE):
    _pack_ = 1
    _fields_ = [
        ("security_code", WORD),
        ("avatar_info", AVATAR_INFO * MAX_AVATAR_COUNT)
    ]
    def __init__(self) -> None:
        self.packet_length = sizeof(AVATAR_LIST)
        self.packet_type = 0x1103
        self.packet_serial = 0

        