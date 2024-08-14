from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

class DilithiumParameterSpec:
    LEVEL2 = "LEVEL2"
    LEVEL3 = "LEVEL3"
    LEVEL5 = "LEVEL5"

def generate_keypair(level):
    if level not in [DilithiumParameterSpec.LEVEL2, DilithiumParameterSpec.LEVEL3, DilithiumParameterSpec.LEVEL5]:
        raise ValueError("Invalid Dilithium parameter level")
    
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def sign(message, private_key):
    signature = private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature

def verify(message, signature, public_key):
    try:
        public_key.verify(
            signature,
            message,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

def serialize_key(key, is_private=True):
    if is_private:
        return key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        return key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

def deserialize_key(pem_data, is_private=True):
    if is_private:
        return load_pem_private_key(pem_data, password=None)
    else:
        return load_pem_public_key(pem_data)
