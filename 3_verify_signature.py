from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

with open("message.txt", "rb") as f:
    message = f.read()

with open("signature.bin", "rb") as f:
    signature = f.read()

tamper = input("Tamper message? (yes/no): ").lower()

if tamper == "yes":
    message = b"THIS MESSAGE WAS CHANGED!"

try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("VALID")
except InvalidSignature:
    print("INVALID")