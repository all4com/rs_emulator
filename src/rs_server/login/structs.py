from typing import Any
from common.network.packets.regular import PACKET_BASE
from ctypes import LittleEndianStructure, sizeof
from ctypes.wintypes import WORD, CHAR, DWORD, UINT
import random

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
IP_SIZE = 16

class AVATAR_INFO(LittleEndianStructure):
    _pack_ = 2
    _fields_ = [
        ("m_wAvatarIndex", WORD),
        ("m_strName", CHAR * NAME_LENGTH),
        ("m_wJob", WORD),
        ("m_wLevel", WORD),
        ("m_wWeapon", WORD),
        ("m_wShield", WORD),
        ("m_wArmor", WORD),
        ("m_wLastField", WORD),
        ("m_strIP", CHAR * IP_SIZE)
    ]

    def __init__(self) -> None:
        self.m_wAvatarIndex = 0xFFFF
        self.m_strName = b'\xFF' * NAME_LENGTH
        self.m_wJob = 0xFFFF
        self.m_wLevel = 0xFFFF
        self.m_wWeapon = 0xFFFF
        self.m_wShield = 0xFFFF
        self.m_wArmor = 0xFFFF
        self.m_wLastField = 0xFFFF
        self.m_strIP = b'\x00' * IP_SIZE
        

class AVATAR_LIST(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("base", PACKET_BASE),
        ("security_code", WORD),
        ("avatar_info", AVATAR_INFO * MAX_AVATAR_COUNT)
    ]
    def __init__(self) -> None:
        self.base = PACKET_BASE()
        self.base.packet_length = sizeof(AVATAR_LIST)
        self.base.packet_type = 0x1103
        self.base.packet_serial = 0
        self.security_code = random.randint(1, 0x6FFF)

        self.avatar_info = (AVATAR_INFO * MAX_AVATAR_COUNT)()
        for i in range(MAX_AVATAR_COUNT):
            avatar = AVATAR_INFO()
            self.avatar_info[i] = avatar


class CREATE_AVATAR(LittleEndianStructure) :
    _pack_ = 1
    _fields_ = [
        ("wJob", WORD),
        ("wSecurityCode", WORD),
        ("uiSecurityCodeRet", UINT),
        ("strName", CHAR * NAME_LENGTH)
    ]
    def __init__(self):
        self.wJob = 0
        self.wSecurityCode = 0
        self.uiSecurityCodeRet = 0
        self.strName = b''