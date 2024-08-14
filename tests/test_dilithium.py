import unittest
from src.dilithium import generate_keypair, sign, verify, serialize_key, deserialize_key, DilithiumParameterSpec

class TestDilithium(unittest.TestCase):

    def setUp(self):
        # Initialize parameters for tests
        self.specs = [
            DilithiumParameterSpec.LEVEL2,
            DilithiumParameterSpec.LEVEL3,
            DilithiumParameterSpec.LEVEL5
        ]

    def test_key_generation(self):
        for spec in self.specs:
            private_key, public_key = generate_keypair(spec)
            self.assertIsNotNone(private_key)
            self.assertIsNotNone(public_key)
            self.assertTrue(hasattr(private_key, 'sign'))
            self.assertTrue(hasattr(public_key, 'verify'))

    def test_sign_and_verify(self):
        for spec in self.specs:
            private_key, public_key = generate_keypair(spec)
            message = b"test message"
            signature = sign(message, private_key)
            self.assertTrue(verify(message, signature, public_key))

            # Test verification with a different public key
            alt_private_key, alt_public_key = generate_keypair(spec)
            self.assertFalse(verify(message, signature, alt_public_key))

            # Test modification detection
            for i in range(len(message)):
                altered_message = bytearray(message)
                altered_message[i] ^= 1
                self.assertFalse(verify(bytes(altered_message), signature, public_key))

    def test_serialization(self):
        for spec in self.specs:
            private_key, public_key = generate_keypair(spec)
            serialized_private_key = serialize_key(private_key, is_private=True)
            serialized_public_key = serialize_key(public_key, is_private=False)

            deserialized_private_key = deserialize_key(serialized_private_key, is_private=True)
            deserialized_public_key = deserialize_key(serialized_public_key, is_private=False)

            message = b"test message"
            signature = sign(message, deserialized_private_key)
            self.assertTrue(verify(message, signature, deserialized_public_key))

if __name__ == "__main__":
    unittest.main()
