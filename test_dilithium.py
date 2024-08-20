import os
import sys

# Adjust the Python path to include the src directory
sys.path.append(os.path.join(os.path.dirname(__file__), 'dilithium/src'))

from dilithium_py.dilithium import Dilithium2

# Step 1: Generate a key pair
pk, sk = Dilithium2.keygen()
print("Public Key:", pk)
print("Secret Key:", sk)

# Step 2: Sign a message
msg = b"Your message signed by Dilithium"
sig = Dilithium2.sign(sk, msg)
print("Signature:", sig)

# Step 3: Verify the signature
is_valid = Dilithium2.verify(pk, msg, sig)
print("Is the signature valid?", is_valid)

# Step 4: Test with an altered message
altered_msg = b"Altered message"
is_valid = Dilithium2.verify(pk, altered_msg, sig)
print("Is the altered message signature valid?", is_valid)
