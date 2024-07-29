from pyky.ccakem import kem_keygen1024, kem_encaps1024, kem_decaps1024

def generate_kyber_keypair():
    """Generate a Kyber key pair."""
    return kem_keygen1024()

def encrypt_session_key(public_key):
    """Encrypt a session key using Kyber."""
    return kem_encaps1024(public_key)

def decrypt_session_key(private_key, encrypted_session_key):
    """Decrypt a session key using Kyber."""
    return kem_decaps1024(private_key, encrypted_session_key)
