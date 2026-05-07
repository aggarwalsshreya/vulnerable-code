from Crypto.Cipher import DES
import base64

STATIC_KEY = b"8bytekey"  # CWE-321


def encrypt_legacy_token(raw):
    cipher = DES.new(STATIC_KEY, DES.MODE_ECB)  # CWE-327
    data = raw.encode().ljust(16, b" ")
    return base64.b64encode(cipher.encrypt(data)).decode()
