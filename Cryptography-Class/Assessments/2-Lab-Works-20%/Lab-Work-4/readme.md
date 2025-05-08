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

**Step 1 & 2: Generate a random key and encrypt a message**  
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

<details>
<summary>Coding explaination</summary>
<br>

**Import Libraries:**
```bash
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
```
`from Crypto.Cipher import AES` :  
We’re using the AES cipher from the pycryptodome library. AES = Advanced Encryption Standard. It’s our main character for encrypting data securely.

`from Crypto.Random import get_random_bytes` :  
We use this to generate strong random bytes, like for the key and IV. These random values make our encryption secure.

`import base64` :  
This is for encoding binary data into text (because binary looks like garbage if you print it raw). We’ll use base64 to turn the key, IV, and ciphertext into nice readable strings.

**Step 1: Generate the AES Key**
```bash
key = get_random_bytes(32)
```
> This generates 32 random bytes (256 bits) = AES-256 key.

**Step 2: Generate IV (Initialization Vector)**
```bash
iv = get_random_bytes(16)
```

> IV = Initialization Vector = extra randomness.

> Always 16 bytes for AES because AES has a block size of 16 bytes.

> It ensures that even if you encrypt the same data twice, you get different results each time.

**Step 3: Create AES Cipher Object**
```bash
cipher = AES.new(key, AES.MODE_CBC, iv)
```
> We're creating a new AES cipher object.

> AES.new(...) takes 3 things:  
the key  
the mode (we're using CBC = Cipher Block Chaining)  
the iv

> This object will now handle encrypting stuff with the given setup.

**Step 4: Prepare the Plaintext**
```bash
plaintext = b"Cryptography Lab by Danish & Raja"
```
> This is the message we want to encrypt.

> The b before the string makes it a byte string (since AES works on bytes, not normal text).

**Step 4.1: Pad the Plaintext**
```bash
pad_len = 16 - len(plaintext) % 16
padded_plaintext = plaintext + bytes([pad_len] * pad_len)
```

> AES needs input in blocks of 16 bytes. So if our message isn’t a perfect multiple of 16, we pad it.

> pad_len calculates how many bytes we need to add.

> bytes([pad_len] * pad_len) creates the padding bytes.
For example, if we need to add 5 bytes, this becomes: b'\x05\x05\x05\x05\x05'.

> This is called PKCS#7 padding.

**Step 5: Encrypt the Padded Plaintext**
```bash
ciphertext = cipher.encrypt(padded_plaintext)
```

> This line encrypts the padded message using the AES cipher we created.

**Step 6: Encode to Base64 for Sharing**
```bash
print("Ciphertext:", base64.b64encode(ciphertext).decode())
print("Key:", base64.b64encode(key).decode())
print("IV:", base64.b64encode(iv).decode())
```
> base64.b64encode(...): converts binary data to readable text.

> .decode(): turns it into a real string we can print.

> Why base64? So we can safely print, copy, or transmit the ciphertext, key, and IV without them getting corrupted.
</details>  
  
**Output:**  
![alt text](screenshots/aes_encryption.png)

**Step 3: Decrypt the message**  
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

See details [here](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%204/lab%204.md#-implementation).

### Task 2: Asymmetric Encryption (RSA)
What is RSA?  
RSA is an asymmetric encryption algorithm. "Asymmetric" means two different keys are used: one to encrypt (public key) and one to decrypt (private key).

**Steps:**
1. Generate RSA keys (Raja will generate them).

2. Encrypt a message with Raja’s public key.

3. Decrypt the message using Raja’s private key.

**Step 1: Raja Generate RSA Keys**  
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

See Raja generate RSA keys [here]()

**Step 2: Encrypt Message with Raja’s Public Key**  
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

<details>
<summary>Coding explaination</summary>
<br>

**Import Libraries:**
```bash
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
```

`from Crypto.PublicKey import RSA`  
This lets us work with RSA keys (public/private).
RSA = Rivest–Shamir–Adleman, a public-key encryption algorithm.

`from Crypto.Cipher import PKCS1_OAEP`  
This is a secure padding scheme used with RSA. It makes sure encryption is random and safe.
It’s like wrapping your message in a strong bubble.

`import base64`  
Turns binary data into readable strings (so you can print/send it).
Without this, encrypted stuff looks like unreadable binary garbage.

**Step 1: Paste Raja's Public Key**
```bash
public_key_str = '''-----BEGIN PUBLIC KEY-----
... Raja’s public key here ...
-----END PUBLIC KEY-----'''
```

> This is the actual public key string Raja gave to me.

> Public keys are used to encrypt messages.

> Anyone can use this key to send Raja an encrypted message, but only he can decrypt it.

**Step 1.1: Import the RSA Key**
```bash
public_key = RSA.import_key(public_key_str)
```

> This takes the key text above and turns it into a Python object that you can use to encrypt.

> Think of this like loading the public key into your crypto tool.

**Step 2: Create RSA Cipher Object with OAEP**
```bash
cipher_rsa = PKCS1_OAEP.new(public_key)
```
We're creating a cipher object that uses:  

- Raja’s `public_key`

- `PKCS1_OAEP` padding (for security)

**Step 3: Prepare the Message**
```bash
message = b"This message is for Raja!"
```

> This is the message I encrypting.

> The `b` in front means it’s a byte string, not a normal text string.

**Step 3.1: Encrypt the Message**
```bash
ciphertext = cipher_rsa.encrypt(message)
```

> This actually encrypts the message using Raja’s public key.

> Output: `ciphertext`, which is unreadable without base64.

**Step 4: Encode for Sharing**
```bash
print("Encrypted:", base64.b64encode(ciphertext).decode())
```

> `base64.b64encode(ciphertext)`: Converts the encrypted binary into text.

> `.decode()`: Converts the base64 object into a printable string.

> Finally, it prints it out so I can copy and give it to Raja.

</details>

**Output:**
![alt text](screenshots/rsa_encrypted.png)
> ScA1VOwk5IhOOxCcNwVVM2HJDO2ni6oxAI8lyVXndS5bJSppDKUuQ+fwTVSQQbsaHTJXrXEnStV7EVK/cn1HqGCEmkg+aUZ3I+FY97upXRAaG92Lvh8Zgfy2HN4gZofbcrGvdMlniGAUszP5M2wcjtO4e2IbswKNTf0uaJrUIqZn3eNMFSqArrMAo4eIoAoJ3f61jIkeUTJB8sJHvzVXkVgcjFY7zLlU+sg3Q0FAqm8Ipi6nKQbyx3JPWMub/aZtZpZER11ThEQfw8+xFKBvaiLlG258VajrCReT8dgseYCeDeCpN3JG90uXP35K0aQ6P+sJysjO1UZTDx0cTYp4NA==

**Step 3: Decrypt Message with Raja’s Private Key**  
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

**Step 1: Hash a message with SHA-256**  
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

<details>
<summary>Coding explaination</summary>
<br>

**Import the Hashing Library:**
```bash
import hashlib
```

> This brings in Python's built-in hashlib module.

> `hashlib` supports many hash functions like `MD5`, `SHA-1`, `SHA-256`, etc.

**Step 1: Define Input Strings**
```bash
data1 = "hello"
data2 = "hello world"
```

> data1 and data2 are just two different pieces of text.

> I will hash them separately to see how different the outputs are (even for small input changes).

**Step 2: Hash the Inputs with SHA-256**
```bash
hash1 = hashlib.sha256(data1.encode()).hexdigest()
hash2 = hashlib.sha256(data2.encode()).hexdigest()
```

> `data1.encode()`: Converts the string into bytes because hashing functions require binary input.

> `hashlib.sha256(...)`: Creates a SHA-256 hash object using that byte input.

> `.hexdigest()`: Converts the binary hash output into a hex string so it’s human-readable.

So basically:

> You're taking your input text → converting to bytes → hashing → converting result to hex string.

**Step 3: Print the Hashes**
```bash
print("Hash of data1:", hash1)
print("Hash of data2:", hash2)
```

> Just shows the hash of each string.

> Showing how even a tiny change in the input causes a huge change in the hash (called the avalanche effect).

</details>

**Step 2: Display the hash value**
```bash
➜ & C:/Users/nishd/AppData/Local/Programs/Python/Python311/python.exe c:/Users/nishd/Downloads/Crypto/Danish/Danish/Cryptography-Class/Assessments/2-Lab-Works-20%/Lab-Work-4/src/hashing.py
Hash of data1: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
Hash of data2: b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
```

![alt text](screenshots/hashing.png)

### Task 4: Digital Signatures (RSA)
What is a Digital Signature?  
A digital signature is used to prove the authenticity of a message. The sender signs the message with their private key, and the recipient can verify it with the sender's public key.

**Steps:**
1. Sign the message using Raja's private key.

2. Verify the signature using Raja's public key.

**Step 1: Raja Signs the .txt File**  
See how Raja signs the .txt file [here]()

**Step 2: Danish Verify the Signature**  
**verify.py**
```bash
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64

# 1. Raja's public key (use the key you shared earlier)
public_key_str = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1JqRbGfSKHggm4rllcd7
WnsCa4Pm7y4/4xw01+pNI3gtWXOvLX3xU3E9CdQzU8U7rFG3e8on4D7CleQdDclW
am92Qn4wcC16oWqwhwrWP3+krvYjKEFx7pMMvvg/Jc/shnyjugNogyN7guhtMsdf
UDOsxOsk4GN/1iW0oOfrNnm7DrhWMa6yL9lKIjnLr96jZOUSRl7+tld5nRwvsDmL
cgl5oGM+KMWi6hcsn/lvzGz+i53j74oaI9uAMRtfd5bvaRg6vjUQQun9gp1CdJ0h
o3+qWDWZqcE0ew7xCpO40sbVwY2B3Y7XAFAp81vPLFalnGVBa70SP7tMVvRDRimJ
0wIDAQAB
-----END PUBLIC KEY-----'''

# 2. Load the message from the txt file (the same one Raja signed)
filename =r"C:\Users\nishd\Downloads\Crypto\Danish\Danish\Cryptography-Class\Assessments\2-Lab-Works-20%\Lab-Work-4\src\digital_file.txt"
with open(filename, "rb") as f:
    file_data = f.read()

# 3. Load the signature from the saved file
with open(r"C:\Users\nishd\Downloads\Crypto\Danish\Danish\Cryptography-Class\Assessments\2-Lab-Works-20%\Lab-Work-4\src\file_signature.txt", "r") as sig_file:
    signature_b64 = sig_file.read()

signature = base64.b64decode(signature_b64)

# 4. Create the hash of the original file data
hash = SHA256.new(file_data)

# 5. Load Raja's public key to verify the signature
public_key = RSA.import_key(public_key_str)

# 6. Verify the signature
try:
    pkcs1_15.new(public_key).verify(hash, signature)
    print("Signature is VALID. The file is authentic.")
except (ValueError, TypeError):
    print("Signature is INVALID. The file may have been tampered with.")
```

**Output:**
```bash
➜ & C:/Users/nishd/AppData/Local/Programs/Python/Python311/python.exe c:/Users/nishd/Downloads/Crypto/Danish/Danish/Cryptography-Class/Assessments/2-Lab-Works-20%/Lab-Work-4/src/verify.py
Signature is VALID. The file is authentic.
```

![alt text](screenshots/verify.png)