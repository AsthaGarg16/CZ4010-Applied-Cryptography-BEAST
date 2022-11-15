from Crypto.Cipher import AES
from Crypto import Random
import string
import random


BLOCK_SIZE = AES.block_size
ALPHANUMERIC = string.digits + string.ascii_letters

class CryptoUtils:
    AES_KEY = b''

    @staticmethod
    def generate_cookie(length):
        return ''.join((random.choice(ALPHANUMERIC) for i in range(length)))
    
    @staticmethod
    def pad(msg, bs=BLOCK_SIZE):
        pad_l = bs - len(msg) % bs
        if isinstance(msg, str):
            return msg + chr(97 + pad_l) * pad_l
        else:
            return msg + bytes(chr(97 + pad_l) * pad_l, "ascii")


    @staticmethod
    def unpad(msg):
        x = msg[-1]
        if isinstance(x, int):
            pad_l = x - 97
        else:
            pad_l = ord(x) - 97
        return msg[:-pad_l]

    @staticmethod
    def xor_block(block1, block2, block3):
        res = b''
        for c1, c2, c3 in zip(block1, block2, block3):
            res += bytes([c1 ^ c2 ^ c3])
        return res

    @staticmethod
    def encrypt(msg, IV=None):
        if not IV:
            IV = Random.new().read(BLOCK_SIZE)
            cipher = AES.new(CryptoUtils.AES_KEY, AES.MODE_CBC, IV)
        if isinstance(CryptoUtils.pad(msg), str):
            return IV + cipher.encrypt(str.encode(CryptoUtils.pad(msg)))
        else:
            return IV + cipher.encrypt(CryptoUtils.pad(msg))

    @staticmethod
    def decrypt(msg_with_IV):
        IV = msg_with_IV[:BLOCK_SIZE]
        msg = msg_with_IV[BLOCK_SIZE:]
        cipher = AES.new(CryptoUtils.AES_KEY, AES.MODE_CBC, IV)
        return CryptoUtils.unpad(cipher.decrypt(msg))
