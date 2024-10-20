from ctypes import *
from ctypes.wintypes import *
from typing import Any
from common.helpers import type_hints


class PACKET_BASE(LittleEndianStructure) :
    _pack_ = 1
    _fields_ = [
        ("packet_length", WORD),
        ("packet_type", WORD),
        ("packet_serial", WORD)
    ]
    def __init__(self) -> None:
        self.packet_length = 0
        self.packet_type = 0
        self.packet_serial = 0

class PACKET_SERVER_TYPE(PACKET_BASE) :
    _pack_ = 1
    _fields_ = [
        ("server_type", WORD),
    ]