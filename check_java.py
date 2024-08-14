import jpype
import jpype.imports
from jpype.types import *
from jpype import JClass

# Get default JVM path

# Start JVM
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=.")

# Import Java classes
Example = JClass("Example")

result = Example.add(10, 5)
print(f"Result of add(10, 5): {result}")

# Shutdown JVM
jpype.shutdownJVM()
