try:
    from pyky.ccakem import kem_keygen512
    print("pyky package is accessible.")
except ImportError:
    print("pyky package is not accessible.")
