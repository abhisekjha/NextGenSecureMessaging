from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_decrypt(encrypted_message, session_key):
    """Decrypt an AES-256 encrypted message."""
    iv = encrypted_message[:16]
    cipher = AES.new(session_key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message[16:]), AES.block_size)
    return decrypted_message
