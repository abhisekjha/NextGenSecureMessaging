import os
import sys

# Adding the path to the Dilithium library
sys.path.append(os.path.join(os.path.dirname(__file__), '../dilithium/src'))

from dilithium_py.dilithium import Dilithium2

# Step 1: Key Generation by Certificate Authority (CA)
##### CERTIFICATE AUTHORITY #####


CA1_pk, CA1_sk = Dilithium2.keygen()

# Step 2: Bob generates a key pair and signs his public key using the CA's secret key
##### BOB #####
bob_pk, bob_sk = Dilithium2.keygen()
bob_sig = Dilithium2.sign(CA1_sk, bob_pk) 
print("####  CA signs Bob's public key ####")




# Step 3: Alice verifies Bob's signature using the CA's public key

is_valid = Dilithium2.verify(CA1_pk, bob_pk, bob_sig)  # Verify Bob's signature using CA's public key

print("Is Bob's signature valid (verified by Alice)?", is_valid)

print("***Alice knows Bob is Authentic using CA****\n")


##### ALICE #####
CA2_pk, CA2_sk = Dilithium2.keygen()
alice_pk, alice_sk = Dilithium2.keygen()


# Step 4: Alice signs the key using ca and sends it to bob
print("####  CA signs Alice's public key ####")
alice_sig = Dilithium2.sign(CA2_sk, alice_pk) 


# Step 5: Bob verifies Alice's signature using the CA's public key

##### BOB #####
is_valid_alice = Dilithium2.verify(CA2_pk, alice_pk, alice_sig)
print("Is Alice's signature valid (verified by Bob)?", is_valid_alice)

print("**** Bob knows Alice is Authentic using CA ****")


