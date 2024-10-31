from ctypes import *
from ctypes.wintypes import *
from typing import Any
from common.helpers import type_hints


class PACKET_BASE(LittleEndianStructure) :
    _pack_ = 1
    _align_ = 1
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


JOB_NAME = {
    0: "dJOB_KNIGHT",
    1: "dJOB_WARRIOR",
    2: "dJOB_WIZARD",
    3: "dJOB_WEREWOLF",
    4: "dJOB_PRIEST",
    5: "dJOB_FALLEN_ANGEL",
    6: "dJOB_ROGUE",
    7: "dJOB_FIGHTER",
    8: "dJOB_MAGIC_LANCER",
    9: "dJOB_MAGIC_ARCHER",
    10: "dJOB_BEAST_TAMER",
    11: "dJOB_SUMMONER",
    12: "dJOB_PRINCESS",
    13: "dJOB_MAGICAL_GIRL",
    14: "dJOB_NECROMANCER",
    15: "dJOB_DEVIL",
    16: "dJOB_SOUL_BRINGER",
    17: "dJOB_CHAMPION",
    18: "dJOB_OPTICALIST",
    19: "dJOB_BEAST_MAN"
}