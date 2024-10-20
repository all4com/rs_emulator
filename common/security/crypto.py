from common.security.xorinfo import XOR_KEYS, DATA_TABLE

ENCRYPTION_KEY_JP = 2
ENCRYPTION_KEY_EN = 1

class CryptRandom:
    MULTIPLIER = 0x343FD
    ADDEND = 0x269EC3
    SHIFT_VALUE = 0x10
    MASK_VALUE = 0x7FFF

    def __init__(self, seed: int):
        self.seed = seed

    def next(self, max_value: int) -> int:
        self.seed = self.seed * self.MULTIPLIER + self.ADDEND
        result = (self.seed >> self.SHIFT_VALUE) & self.MASK_VALUE
        return result % max_value


class CryptoUtils:
    EncryptionKey = [0x6F, 0x40]
    RANDOM_OFFSET = 0x7C
    PACKET_SIZE = 0x2
    DECODEKEY_SIZE = 0x4

    def __init__(self, data: bytes):
        self.cipher = bytearray(data)
        self.packet_length = self.cipher[:self.PACKET_SIZE]
        self.cipher = self.cipher[self.PACKET_SIZE:]
        self.decode_key_bytes = self.cipher[:self.DECODEKEY_SIZE]
        self.cipher_id = int.from_bytes(self.decode_key_bytes, 'little')
        self.cipher = self.cipher[self.DECODEKEY_SIZE:]

    def decrypt(self) -> bytearray:
        random = CryptRandom(self.cipher_id)
        range_ = self.cipher_id % self.EncryptionKey[0] + self.EncryptionKey[1]
        self.cipher = bytearray([(byte - (random.next(range_) + self.RANDOM_OFFSET)) & 0xFF for byte in self.cipher])
        return self.cipher

    def encrypt(self) -> bytearray:
        random = CryptRandom(self.cipher_id)
        range_ = self.cipher_id % self.EncryptionKey[0] + self.EncryptionKey[1]
        self.cipher = bytearray([(byte + (random.next(range_) + self.RANDOM_OFFSET)) & 0xFF for byte in self.cipher])
        return self.cipher

    @staticmethod
    def decode_login_string(security_code: int, data: bytes) -> str:
        encryption_seed = 100
        rand = CryptRandom(security_code)
        range_ = security_code % encryption_seed + encryption_seed
        decoded = []
        for byte in data:
            rand_a = rand.next(range_)
            decoded_byte = (byte - rand_a) & 0xFF 
            decoded.append(decoded_byte)
        return bytes(decoded)

    @staticmethod
    def generate_decode_key(seed: int) -> int:
        if (seed == -1) :
            return 0
        if (seed != 1) :
            return 1
        else :
            return 2

    @staticmethod
    def decode_scenario_data(data: bytearray, decode_key: int) -> bytearray:
        result = bytearray(len(data))
        table_offset = ((decode_key * 9) << 3) - decode_key
        table_offset = table_offset & 0xFF

        counter = 0
        piece_length = 0x47
        for i in range(len(data)):
            result_data = (DATA_TABLE[counter + table_offset] + XOR_KEYS[counter + table_offset]) & 0xFF
            result[i] = data[i] ^ result_data
            counter += 1
            if counter >= piece_length:
                counter = 0
        return result
