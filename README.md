# Secure Messaging with Kyber, Dilithium, and AES-256

This project demonstrates how to securely encrypt packets of messages using AES-256 encryption. Keys are securely exchanged using Kyber, a post-quantum cryptographic algorithm, and authenticated using Dilithium ensuring protection against both classical and quantum attacks.

## Check Out the Webpage to Learn More

[![Website](https://img.shields.io/badge/Website-pqc_aes_multipath-red?style=flat-square)](https://www.abhisekjha.com.np/NextGenSecureMessaging)

## Steps to Run the Test

1. **Activate the environment**
   ```bash
   source venv/bin/activate
   ```

2. Git clone the `pqc_aes_multipath` repo:
```bash
https://github.com/abhisekjha/NextGenSecureMessaging.git
cd pqc_aes_multipath
```

3. git clone `Kyber based PYKY`
```bash
https://github.com/asdfjkl/pyky.git
```


4. Set and verify Pythonpath:
``` sh
export PYTHONPATH=/path/to/pqc_aes_multipath:/path/to/pqc_aes_multipath/pyky:/path/to/pqc_aes_multipath/dilithium-java
echo $PYTHONPATH
```

5. Set the JAVA_HOME to other version()
```sh
export JAVA_HOME=`/usr/libexec/java_home -v 11`
export PATH=$JAVA_HOME/bin:$PATH
```

6. Build the dilithium project:
```cd dilithium-java
mvn clean install
```

7. Set Java environment for JDK 8 and build with Gradle:
```sh
/usr/libexec/java_home -v 1.8
export BC_JDK8=/Library/Java/JavaVirtualMachines/temurin-8.jdk/Contents/Home
export JAVA_HOME=$BC_JDK8
export PATH=$JAVA_HOME/bin:$PATH

java -version
./gradlew clean
./gradlew build --refresh-dependencies

```

8. Install requirements.txt
```
pip install -r requirements.txt
```
8. Run test cases using make
```
make
```

## Acknowledgements

I would like to thank the [pyky](https://github.com/asdfjkl/pyky) repository and [dilithium-py](https://github.com/GiacomoPope/dilithium-py) for providing the implementation of the Kyber cryptographic algorithm and Dilithium Implementation, which was used in this project.
