import time
from tqdm import tqdm
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from src.key_management import generate_kyber_keypair, encrypt_session_key, decrypt_session_key
from src.encryption import generate_aes_key, aes_encrypt
from src.decryption import aes_decrypt


# Convert list of signed integers to bytes
def convert_to_bytes(signed_int_list):
    return bytes([x & 0xFF for x in signed_int_list])

def loading_message(message, duration=0.1):
    """Simulate a loading process with a message and duration."""
    print(message)
    for _ in tqdm(range(100), desc=message, ncols=100, ascii=True, bar_format='{l_bar}{bar} | {percentage:3.0f}%'):
        time.sleep(duration / 100)
    print()

def test_main():

#1. Key Exchange
#2. exchange message
#3. dilithujm signature come into play to verify the message embedded in the cipher text


    #generate Kyber key pair for Alice

#bob
    loading_message("1. Generating Kyber key pair...(Receiver)")
    priv_key, pub_key = generate_kyber_keypair()
    print("Kyber key pair generated.\n")

### Key exchange


# Alice

    #encrypt AES session key with Kyber public key
    loading_message("2. Encrypting session key with Kyber public key...(Sender)")
    shared_secret, cipher = encrypt_session_key(pub_key)
    print("AES session key encrypted with Kyber public key.\n")

    #get Symmetric key for AES
    loading_message("3. AES session key...(Sender)")
    aes_key = convert_to_bytes(shared_secret)
    print("AES session key generated.\n")




    #encrypt a sample message with AES
    loading_message("Encrypting message with AES...(Sender)")

    message = b"Hello, this is a test message!"
    encrypted_message = aes_encrypt(message, aes_key)

    print("Message encrypted with AES.\n")

## Note: Along with the encrypted message, the sender also sends the cipher text of the AES session key to the receiver.


# BOB



    #decrypt AES session key with Kyber private key
    loading_message("Decrypting AES symmetric key with Kyber private key and cipher text...(Receiver)")
    decrypted_aes_key = decrypt_session_key(priv_key, cipher)
    print("AES session key decrypted with Kyber private key.\n")

    #decrypt the message with the decrypted AES key
    loading_message("Decrypting message with AES...(Receiver)")
    decrypted_message = aes_decrypt(encrypted_message, convert_to_bytes(decrypted_aes_key))
    print("Message decrypted with AES.\n")


## 

    #check if the original message and decrypted message are the same
    assert message == decrypted_message, "Decryption failed: original and decrypted messages do not match!"
    print("Encryption and decryption test passed!")

    print("Original Message:", message)
    print("Decrypted Message:", decrypted_message)
    print("***TEST***=",message==decrypted_message)

if __name__ == "__main__":
    loading_message("***This is the general test for Encryption and DEcryption using Kyber and AES.***", duration=1)
    test_main()
    print("Test completed successfully!")