import os
import sys

# Adding the path to the Dilithium library
sys.path.append(os.path.join(os.path.dirname(__file__), '../dilithium/src'))

from dilithium_py.dilithium import Dilithium2

# Step 1: Key Generation by Certificate Authority (CA)
##### CERTIFICATE AUTHORITY ######
CA_pk, CA_sk = Dilithium2.keygen()

# Step 2: Bob generates a key pair and signs his public key using the CA's secret key
##### BOB #####
bob_pk, bob_sk = Dilithium2.keygen()
bob_sig = Dilithium2.sign(CA_sk, bob_pk)  # CA signs Bob's public key
print("Bob's Public Key:", bob_pk)
print("Bob's Signature (signed by CA):", bob_sig)

# Step 3: Alice generates her key pair and verifies the signature on Bob's public key using the CA's public key
##### ALICE #####
alice_pk, alice_sk = Dilithium2.keygen()
is_valid = Dilithium2.verify(CA_pk, bob_pk, bob_sig)  # Verify Bob's signature
print("Is Bob's signature valid (verified by Alice)?", is_valid)

##### Mutual direct authentication

# Step 4: Alice sends her public key to Bob, and Bob signs it with his secret key
alice_sig = Dilithium2.sign(bob_sk, alice_pk)  # Bob signs Alice's public key
print("Alice's Public Key:", alice_pk)
print("Alice's Signature (signed by Bob):", alice_sig)

### Bob sends signated Alice public key to Alice

# Alice already has Bob's public key and now he has Bob's signature on Alice public key, authenticated by Bob

# Step 5: Bob verifies Alice's public key signature using his public key
is_valid_alice = Dilithium2.verify(bob_pk, alice_pk, alice_sig)
print("Is Alice's signature valid (verified by Bob)?", is_valid_alice)

# Step 6: Test with an altered message; the signature should be invalid
altered_msg = b"Altered message"
is_valid_altered = Dilithium2.verify(bob_pk, altered_msg, bob_sig)
print("Is the altered message signature valid?", is_valid_altered)

# Step 7: Test with an altered signature; the signature should also be invalid
altered_sig = bob_sig[:-1] + bytes([bob_sig[-1] ^ 0x01])  # Tamper with the signature
is_valid_tampered_sig = Dilithium2.verify(CA_pk, bob_pk, altered_sig)
print("Is the tampered signature valid?", is_valid_tampered_sig)

# Step 8: Final mutual authentication and key exchange demonstration
# Both parties (Alice and Bob) can now use each other's verified public keys for secure communication
