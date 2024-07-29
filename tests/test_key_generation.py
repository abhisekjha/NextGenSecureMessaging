from src.key_management import generate_kyber_keypair

# Generate Kyber key pair
private_key, public_key = generate_kyber_keypair()
print("Private Key:", private_key)
print("Public Key:", public_key)
