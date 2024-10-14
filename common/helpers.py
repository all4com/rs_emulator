from ctypes import *
from ctypes.wintypes import *

def print_binary(binary: bytes) -> None:
    hex_string = ''.join(hex(byte)[2:].zfill(2).upper() for byte in binary)
    print(hex_string)

def int_to_little_endian_hex(value: int) -> str:
    length = (value.bit_length() + 7) // 8 or 1
    byte_array = value.to_bytes(length, byteorder='big')
    return f"0x{byte_array.hex()}"

def type_hints(cls):
    for field_name, field_type in cls._fields_:
        if field_type == WORD:
            hint_type = int
        elif field_type == DWORD:
            hint_type = int
        elif field_type == CHAR:
            hint_type = str
        elif field_type == SHORT:
            hint_type = int
        setattr(cls, field_name, hint_type)


