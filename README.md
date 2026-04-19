# Digital-signature


This project is a simple implementation of digital signatures using RSA cryptography in Python. It is created for learning purposes to understand how authentication and data integrity work in computer security.
The system demonstrates how a message can be signed using a private key and then verified using a public key. If the message is changed after signing, the verification will fail, showing that the data has been tampered with.

How it works

First, the key generation program creates a pair of keys: a private key and a public key. The private key is kept secret and is used to sign messages. The public key is shared and is used to verify signatures.
Next, the signing program takes a message from the user and creates a digital signature using the private key. It then saves both the message and the signature.
Finally, the verification program checks whether the signature matches the message using the public key. The user also has the option to simulate tampering with the message to see how the system detects changes.

Files in the project

1_generate_keys.py
This file generates the private and public keys and saves them as files.

2_sign_message.py
This file takes a message from the user and creates a digital signature.

3_verify_signature.py
This file checks whether the signature is valid or not. It can also simulate message tampering.

private_key.pem
This file stores the private key.

public_key.pem
This file stores the public key.

message.txt
This file stores the original message that was signed.

signature.bin
This file stores the generated digital signature.

How to run

Run the files in this order:

First run 1_generate_keys.py
Then run 2_sign_message.py
Finally run 3_verify_signature.py

What you will learn

This project helps you understand the basics of public key cryptography, digital signatures, and how data integrity is maintained in secure systems. It also shows what happens when data is modified after being signed.

Note
This project is for educational purposes only and is not intended for production use.
