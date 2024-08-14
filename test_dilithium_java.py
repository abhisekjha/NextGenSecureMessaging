import jpype
import jpype.imports
from jpype.types import *

# Path to the JAR file
classpath = '/Users/abhisekjha/MyFolder/Github_Projects/NextGenSecureMessaging/dilithium-java/'

# # Manually specify the JVM path (using JAVA_HOME)
# jvm_path = f'{os.environ["JAVA_HOME"]}/jre/lib/server/libjvm.dylib'

# # Print JVM path to verify it's correct
# print(f"JVM Path: {jvm_path}")

# Start the JVM with the specified path
jpype.startJVM(classpath=classpath)

# Import and use your Java wrapper
from dilithium.DilithiumWrapper import DilithiumWrapper

# Create an instance of DilithiumWrapper
wrapper = DilithiumWrapper()

# Example usage
message = b"Hello, Dilithium!"
signature = wrapper.sign(message)
verification = wrapper.verify(message, signature)
print(f"Verification result: {verification}")

# Shutdown the JVM
jpype.shutdownJVM()
