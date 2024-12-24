# Makefile

all: script1 script2 script3 script4 script5 

script1:
	python3 tests/test_encryption.py

script2:
	python3 tests/test_decryption.py

script3:
	python3 tests/test_key_generation.py

script4:
	python3 tests/test_main.py

# script5:
# 	python3 tests/test_pqc_multipath.py

script5:
	python3 tests/test_dilithium.py