import os
from src.encryption import generate_aes_key, aes_encrypt
from src.decryption import aes_decrypt
from src.key_management import generate_kyber_keypair, encrypt_session_key, decrypt_session_key
from tqdm import tqdm
import time

def loading_message(message, duration=0.1):
    """Simulate a loading process with a message and duration."""
    print(message)
    for _ in tqdm(range(100), desc=message, ncols=100, ascii=True, bar_format='{l_bar}{bar} | {percentage:3.0f}%'):
        time.sleep(duration / 100)
    print()

folder_path = '/Users/abhisekjha/Multipath_Research/PQC/pqc_aes_multipath/data/input'
files = os.listdir(folder_path)



def convert_to_bytes(signed_int_list):
    return bytes([x & 0xFF for x in signed_int_list])

def pqc_multipath():

    loading_message("0. Reading Encoded Message from Input folder")
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'rb') as file:
            M = file.read()


    #kyber keys
    loading_message("1. Generating Kyber Key Pair")
    private_key, public_key = generate_kyber_keypair()

    aes_key, cipher= encrypt_session_key(public_key)

    loading_message("2. Encrypt the message")
    encrypted_message = aes_encrypt(M, convert_to_bytes(aes_key))


    loading_message("3. Decrypt the aes key with kyber private key")
    decrypted_aes_key = decrypt_session_key(private_key, cipher)

    loading_message("4. Decrypt the message")
    decrypted_message = aes_decrypt(encrypted_message, convert_to_bytes(decrypted_aes_key))

    print("***Is Original Message and Decrypted Message SAME***??=>", M == decrypted_message)

if __name__== "__main__":
    pqc_multipath()
    print("PQC Multipath Done")