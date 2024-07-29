import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def generate_aes_key():
    """Generate a random AES session key."""
    return os.urandom(32)

def aes_encrypt(message, session_key):
    """Encrypt a message using AES-256."""
    cipher = AES.new(session_key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_message = cipher.encrypt(pad(message, AES.block_size))
    return iv + encrypted_message
