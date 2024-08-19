import jpype
import jpype.imports
from jpype.types import *
from jpype import JClass, JPackage


jar_path = "/Users/abhisekjha/MyFolder/Github_Projects/NextGenSecureMessaging/dilithium-java/target/dilithium-java-0.0.1-SNAPSHOT.jar"


bouncy_castle_jar_path = "/bcprov-jdk15on-VERSION.jar"

try:
    
    jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", f"-Djava.class.path={jar_path}:{bouncy_castle_jar_path}")

    
    from java.security import Security
    DilithiumProvider = JClass("net.thiim.dilithium.provider.DilithiumProvider")
    Security.addProvider(DilithiumProvider())

    
    KeyPairGenerator = JClass("java.security.KeyPairGenerator")
    Signature = JClass("java.security.Signature")
    DilithiumParameterSpec = JClass("net.thiim.dilithium.interfaces.DilithiumParameterSpec")

    
    spec = DilithiumParameterSpec.LEVEL2  # Use LEVEL2 

    
    kpg = KeyPairGenerator.getInstance("Dilithium")
    kpg.initialize(spec)
    key_pair = kpg.generateKeyPair()

    public_key = key_pair.getPublic()
    private_key = key_pair.getPrivate()
    print(f"Public key: {public_key}")
    print(f"Secret key: {private_key}")

    # Sign a message
    message = "Hello, World!".encode("utf-8")  
    signature = Signature.getInstance("Dilithium")
    signature.initSign(private_key)
    signature.update(message)
    sig_bytes = signature.sign()
    print(f"Signature: {sig_bytes}")

    # Verify the signature
    verifier = Signature.getInstance("Dilithium")
    verifier.initVerify(public_key)
    verifier.update(message)
    is_valid = verifier.verify(sig_bytes)
    print(f"Is valid: {is_valid}")

    # Modify the message and verify the signature again to check robustness against tampering
    altered_message = "Hello, World?".encode("utf-8")
    verifier.update(altered_message)
    is_altered_valid = verifier.verify(sig_bytes)
    print(f"Is altered message valid: {is_altered_valid}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
   
    jpype.shutdownJVM()
