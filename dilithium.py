import jpype
import jpype.imports
from jpype.types import *

class DilithiumWrapper:
    def __init__(self):
        # Start the JVM
        jpype.startJVM(classpath=['./dilithium-java/target/dilithium-java.jar'])

        # Import your Java class
        from com.example.dilithium import DilithiumWrapper as JavaDilithiumWrapper
        self.java_wrapper = JavaDilithiumWrapper()

    def example_method(self):
        return self.java_wrapper.exampleMethod()
