import jpype
import jpype.imports
from jpype.types import *
from jpype import JClass

# Ensure you specify the correct path to the .jar file that contains the Dilithium implementation
jar_path = "/Users/abhisekjha/MyFolder/Github_Projects/NextGenSecureMessaging/dilithium-java/target/dilithium-java-0.0.1-SNAPSHOT.jar"

try:
    # Start JVM
    jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", f"-Djava.class.path={jar_path}")
    
    # Import Java classes directly related to the cryptography features
    Dilithium = JClass("net.thiim.dilithium.impl.Dilithium")
    DilithiumParameterSpec = JClass("net.thiim.dilithium.interfaces.DilithiumParameterSpec")
    KeyPair = JClass("java.security.KeyPair")
    Signature = JClass("java.security.Signature")

    # Assume that we need a specification for generating the key pair
    spec = DilithiumParameterSpec.LEVEL2  # Assuming LEVEL2 is a valid spec and accessible

    # Generate key pair
    seed = jpype.JArray(jpype.JByte)(32)  # Example seed, assuming 32 bytes are suitable
    key_pair = Dilithium.generateKeyPair(spec, seed)
    
    public_key = key_pair.getPublic()
    private_key = key_pair.getPrivate()
    print(f"Public key: {public_key}")
    print(f"Secret key: {private_key}")

    # Sign message
    message = "Hello, World!".encode("utf-8")  # Message needs to be bytes
    signature = Dilithium.sign(private_key, message)
    print(f"Signature: {signature}")

    # Verify signature
    is_valid = Dilithium.verify(public_key, signature, message)
    print(f"Is valid: {is_valid}")

    # Modify message
    altered_message = "Hello, World?".encode("utf-8")
    is_altered_valid = Dilithium.verify(public_key, signature, altered_message)
    print(f"Is altered message valid: {is_altered_valid}")

except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Shutdown JVM
    jpype.shutdownJVM()
