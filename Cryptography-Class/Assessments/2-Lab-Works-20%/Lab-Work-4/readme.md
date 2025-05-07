# Lab 4: Implementing Cryptography with Python

## A. Objective:  
In this lab, we will implement fundamental cryptographic algorithms, explore security properties, and understand real-world applications like encryption, hashing, and digital signatures. The tasks are split between symmetric encryption (AES), asymmetric encryption (RSA), hashing (SHA-256), and RSA digital signatures.

## B. Lab Tasks:

### Task 1: Symmetric Encryption (AES)
What is AES?  
AES (Advanced Encryption Standard) is a symmetric encryption algorithm. "Symmetric" means the same key is used to encrypt and decrypt the data. In this task, we’ll be using AES to encrypt a message and then decrypt it back to the original message.

**Steps:**
1. Generate a random key (this key will be used for encryption and decryption).

2. Encrypt a message using the key.

3. Decrypt the message back to its original form.

**aes_encryption.py**
```bash
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# 1. Generate a 32-byte key for AES-256
key = get_random_bytes(32)  # 32 bytes = 256 bits

# 2. Create a random Initialization Vector (IV) for CBC mode
iv = get_random_bytes(16)  # AES block size is 16 bytes

# 3. Create AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# 4. Prepare plaintext (must be padded to a multiple of 16 bytes)
plaintext = b"Cryptography Lab by Danish & Raja"
pad_len = 16 - len(plaintext) % 16
padded_plaintext = plaintext + bytes([pad_len] * pad_len)

# 5. Encrypt the plaintext
ciphertext = cipher.encrypt(padded_plaintext)

# 6. Encode ciphertext, IV, and key in base64 to share safely
print("Ciphertext:", base64.b64encode(ciphertext).decode())
print("Key:", base64.b64encode(key).decode())
print("IV:", base64.b64encode(iv).decode())
```

**Output:**  
![alt text](screenshots/aes_encryption.png)

**aes_decryption.py**
```bash
from Crypto.Cipher import AES
import base64

# 1. Paste your values here (from your encryption output)
key = base64.b64decode("tvPrWH2wVHEtBv4NmHNAoyrTKIdHcVGj5clf2V8TE8g=")
iv = base64.b64decode("PUgXpZIefjVR7BuwzsiSCg==")
ciphertext = base64.b64decode("l/+waUOVxpN0OqS5Mibim5mRmqb1Ez0zwsV2cmeZatOP2eYF2cQxMPG4By7LXBjU")

# 2. Create cipher for decryption
cipher = AES.new(key, AES.MODE_CBC, iv)

# 3. Decrypt ciphertext
padded_plaintext = cipher.decrypt(ciphertext)

# 4. Remove padding
pad_len = padded_plaintext[-1]
plaintext = padded_plaintext[:-pad_len]

print("Decrypted:", plaintext.decode())
```

**Output:**  
![alt text](screenshots/aes_decryption.png)

### Task 2: Asymmetric Encryption (RSA)
What is RSA?  
RSA is an asymmetric encryption algorithm. "Asymmetric" means two different keys are used: one to encrypt (public key) and one to decrypt (private key).

**Steps:**
1. Generate RSA keys (Raja will generate them).

2. Encrypt a message with Raja’s public key.

3. Decrypt the message using Raja’s private key.

**rsa_keygen_raja.py**
```bash
from Crypto.PublicKey import RSA

# 1. Generate RSA key pair (2048 bits is standard)
key_pair = RSA.generate(2048)

# 2. Export the private key (keep this secret!)
private_key = key_pair.export_key()
with open("raja_private.pem", "wb") as f:
    f.write(private_key)

# 3. Export the public key (share this with you for encryption)
public_key = key_pair.publickey().export_key()
with open("raja_public.pem", "wb") as f:
    f.write(public_key)

print("RSA key pair generated.")
```

**Output:** Raja generate RSA keys [here]()

**rsa_encryption.py**
```bash
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# 1. Import Raja's public key (paste it here)
public_key_str = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1JqRbGfSKHggm4rllcd7
WnsCa4Pm7y4/4xw01+pNI3gtWXOvLX3xU3E9CdQzU8U7rFG3e8on4D7CleQdDclW
am92Qn4wcC16oWqwhwrWP3+krvYjKEFx7pMMvvg/Jc/shnyjugNogyN7guhtMsdf
UDOsxOsk4GN/1iW0oOfrNnm7DrhWMa6yL9lKIjnLr96jZOUSRl7+tld5nRwvsDmL
cgl5oGM+KMWi6hcsn/lvzGz+i53j74oaI9uAMRtfd5bvaRg6vjUQQun9gp1CdJ0h
o3+qWDWZqcE0ew7xCpO40sbVwY2B3Y7XAFAp81vPLFalnGVBa70SP7tMVvRDRimJ
0wIDAQAB
-----END PUBLIC KEY-----'''

public_key = RSA.import_key(public_key_str)

# 2. Create RSA cipher
cipher_rsa = PKCS1_OAEP.new(public_key)

# 3. Encrypt message
message = b"This message is for Raja!"
ciphertext = cipher_rsa.encrypt(message)

# 4. Encode ciphertext
print("Encrypted:", base64.b64encode(ciphertext).decode())
```

**Output:**
![alt text](screenshots/rsa_encrypted.png)
> ScA1VOwk5IhOOxCcNwVVM2HJDO2ni6oxAI8lyVXndS5bJSppDKUuQ+fwTVSQQbsaHTJXrXEnStV7EVK/cn1HqGCEmkg+aUZ3I+FY97upXRAaG92Lvh8Zgfy2HN4gZofbcrGvdMlniGAUszP5M2wcjtO4e2IbswKNTf0uaJrUIqZn3eNMFSqArrMAo4eIoAoJ3f61jIkeUTJB8sJHvzVXkVgcjFY7zLlU+sg3Q0FAqm8Ipi6nKQbyx3JPWMub/aZtZpZER11ThEQfw8+xFKBvaiLlG258VajrCReT8dgseYCeDeCpN3JG90uXP35K0aQ6P+sJysjO1UZTDx0cTYp4NA==

**rsa_decryption.py**
```bash
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# 1. Load private key
private_key_str = '''-----BEGIN PRIVATE KEY-----
<RAJA'S PRIVATE KEY>
-----END PRIVATE KEY-----'''

private_key = RSA.import_key(private_key_str)

# 2. Decode ciphertext
ciphertext = base64.b64decode("<ENCRYPTED MESSAGE>")

# 3. Decrypt
cipher_rsa = PKCS1_OAEP.new(private_key)
plaintext = cipher_rsa.decrypt(ciphertext)

print("Decrypted:", plaintext.decode())
```
See Raja decrypt [here]()

### Task 3: Hashing (SHA-256)
What is SHA-256?  
SHA-256 is a hashing algorithm that generates a fixed-size hash (digest) from any input. It is one-way: you can't get back the original data from the hash.

**Steps:**
1. Hash a message using SHA-256.

2. Display the hash value.

**hashing.py**
```bash
import hashlib

# Input data
data1 = "hello"
data2 = "hello world"

# Hash
hash1 = hashlib.sha256(data1.encode()).hexdigest()
hash2 = hashlib.sha256(data2.encode()).hexdigest()

print("Hash of data1:", hash1)
print("Hash of data2:", hash2)
```

**Output**  

![alt text](screenshots/hashing.png)

### Task 4: Digital Signatures (RSA)
What is a Digital Signature?  
A digital signature is used to prove the authenticity of a message. The sender signs the message with their private key, and the recipient can verify it with the sender's public key.

**Steps:**
1. Sign the message using Raja's private key.

2. Verify the signature using Raja's public key.

