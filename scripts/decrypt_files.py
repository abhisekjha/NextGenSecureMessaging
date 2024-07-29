import os
from src.key_management import decrypt_session_key
from src.decryption import aes_decrypt
from src.file_utils import read_file, write_file

INPUT_FOLDER = "../data/output"
OUTPUT_FOLDER = "../data/input"

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Use the private key generated previously
    recipient_private_key = ... # Load your private key here

    # Decrypt messages in the "output" folder
    for file_name in os.listdir(INPUT_FOLDER):
        if file_name.endswith('.bin'):
            file_path = os.path.join(INPUT_FOLDER, file_name)
            
            # Read the encrypted session key and message
            encrypted_data = read_file(file_path)
            encrypted_session_key = encrypted_data[:800]  # Adjust size according to Kyber's encapsulation size
            encrypted_message = encrypted_data[800:]  # Rest is the encrypted message
            
            # Decrypt the session key using recipient's private key with Kyber
            decrypted_session_key = decrypt_session_key(recipient_private_key, encrypted_session_key)
            
            # Decrypt the message using AES-256
            decrypted_message = aes_decrypt(encrypted_message, decrypted_session_key)
            
            # Save the decrypted message
            decrypted_file_path = os.path.join(OUTPUT_FOLDER, file_name)
            write_file(decrypted_file_path, decrypted_message)

if __name__ == "__main__":
    main()
