import os
from src.key_management import generate_kyber_keypair, encrypt_session_key
from src.encryption import generate_aes_key, aes_encrypt
from src.file_utils import read_file, write_file

INPUT_FOLDER = "../data/input"
OUTPUT_FOLDER = "../data/output"

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Generate Kyber key pairs
    recipient_public_key, recipient_private_key = generate_kyber_keypair()

    # Encrypt messages in the "input" folder
    for file_name in os.listdir(INPUT_FOLDER):
        if file_name.endswith('.bin'):
            file_path = os.path.join(INPUT_FOLDER, file_name)
            
            # Read the message
            message = read_file(file_path)
            
            # Generate a random AES session key
            aes_session_key = generate_aes_key()
            
            # Encrypt the session key using recipient's public key with Kyber
            encrypted_session_key = encrypt_session_key(recipient_public_key, aes_session_key)
            
            # Encrypt the message using AES-256
            encrypted_message = aes_encrypt(message, aes_session_key)
            
            # Save the encrypted session key and message
            encrypted_file_path = os.path.join(OUTPUT_FOLDER, file_name)
            write_file(encrypted_file_path, encrypted_session_key + encrypted_message)

if __name__ == "__main__":
    main()
