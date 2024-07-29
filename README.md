# Secure Messaging with Kyber and AES-256

This project demonstrates how to securely encrypt packets of messages using AES-256, with the keys being securely exchanged using Kyber, a post-quantum cryptographic algorithm. The process ensures that the encrypted messages are protected against both classical and quantum attacks.

## Check Out the Webpage to learn more

<a href="https://www.abhisekjha.com.np/pqc_aes_multipath">
    <img src="https://img.shields.io/badge/Website-pqc_aes_multipath-red?style=flat-square">
</a>


## Flowchart

```plaintext
+-----------------------+
| Generate Kyber Keys   |
| (Public & Private)    |
+-----------------------+
           |
           V
+-----------------------+
| For each message:     |
| 1. Encrypt session key|
|    with Kyber         |
+-----------------------+
           |
           V
+-----------------------+
| Encrypt message using |
| AES-256 with session  |
| key                   |
+-----------------------+
           |
           V
+-----------------------+
| Store encrypted session|
| key and encrypted      |
| message in a file      |
+-----------------------+
           |
           V
+-----------------------+
| For decryption:       |
| 1. Decrypt session key|
|    with Kyber         |
| 2. Decrypt message    |
|    with AES-256 using |
|    session key        |
+-----------------------+
```

### Usage
- Includes the Encoded files in input folder.
- Test cases can be run by
```make``` 
- Makefile will run below test files.
    - python3 tests/test_encryption.py
    - python3 tests/test_decryption.py
    - python3 tests/test_key_generation.py
    - python3 tests/test_main.py
    - python3 tests/test_pqc_multipath.py 
- tests/test_main.py includes the general test for sample message
- test/test_pqc_multipath includes the test with Multipath encoded files

This script ensures the secure encryption and decryption of messages using a combination of Kyber and AES-256, providing strong security against both current and future threats.

# Steps to Run the Test

1. Activate the environment
```
source venv/bin/activate
```

2. Git clone the `pqc_aes_multipath` repo:
```
https://github.com/abhisekjha/pqc_aes_multipath.git
cd pqc_aes_multipath
```

3. git clone `Kyber based PYKY`
```
https://github.com/asdfjkl/pyky.git
```


4. Set the PYTHONPATH to include the current directory and the pyky directory:
```
export PYTHONPATH=/path/to/pqc_aes_multipath:/path/to/pqc_aes_multipath/pyky
```
5. To Verify PYTHONPATH

```
echo $PYTHONPATH
```

6. Install requirements.txt
```
pip install -r requirements.txt
```
7. Run test cases using make
```
make
```

## Acknowledgements

I would like to thank the [pyky](https://github.com/asdfjkl/pyky) repository for providing the implementation of the Kyber cryptographic algorithm, which was used in this project.
