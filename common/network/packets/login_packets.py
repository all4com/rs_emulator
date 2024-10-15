from ctypes import *
from ctypes.wintypes import *
from common.helpers import type_hints


class PACKET_BASE(LittleEndianStructure) :
    _pack_ = 1
    _fields_ = [
        ("length", WORD),
        ("type", WORD),
        ("serial", WORD),
    ]

class PACKET_SERVER_TYPE(PACKET_BASE) :
    _pack_ = 1
    _fields_ = [
        ("server_type", WORD),
    ]