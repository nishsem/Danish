# Lab 3: Hands-on Exploration of Cryptographic Tools with OpenSSL

## A. Objectives:

This lab introduces to OpenSSL, a widely used cryptography toolkit, for performing essential cryptographic operations such as:

1. Symmetric encryption (AES)
2. Asymmetric encryption (RSA)
3. Hashing (SHA-256)
4. Digital signatures (RSA with SHA-256)

By the end of this lab, students will be able to:

1. Encrypt and decrypt files using symmetric and asymmetric encryption.
2. Generate and verify hashes for data integrity.
3. Create and verify digital signatures.

---

## B. Lab Tasks:

### Task 1: Symmetric Encryption and Decryption using AES-256-CBC
**Goal:** Encrypt a message using a shared key (symmetric encryption) and then decrypt it with the same key.

**Scenario:** Danish wants to send a confidential message to Raja using symmetric encryption.

**Tools Used:**
- OpenSSL (command line)
- Linux shell utilities (echo, cat, diff)

**Commands:**
1. Generate a strong random key
```bash
openssl rand -hex 32 > key.bin
```
> `rand` -hex 32: Generates 32 random bytes in hex (256 bits) — used as AES key.

![alt text](<screenshots/generate_key.jpg>)

![alt text](<screenshots/key.jpg>)

2. Create a plaintext message
```bash
echo "Hello, this is a secret message from Danish." > message.txt
```

3. Encrypt using AES-256-CBC
```bash
openssl enc -aes-256-cbc -salt -in message.txt -out encrypted_message.bin -pass file:./key.bin
```
> - `enc` : Encryption utility

> - `aes-256-cbc` : Specifies AES with 256-bit key in CBC mode

> - `salt` : Adds salt to prevent dictionary attacks

> - `pass file` : ./key.bin: Reads key from file



4. Raja decrypt it back
```bash
openssl enc -aes-256-cbc -d -in encrypted_message.bin -out decrypted.txt -pass file:./key.bin
```
> - d: Decrypt mode

> - Output should match the original

5. Verify
```bash
diff message.txt decrypted.txt
```
There's no output, it means both files are identical.

```bash
cat message.txt decrypted.txt
```

### Task 2: Asymmetric Encryption and Decryption using RSA
**Goal:** Use RSA to encrypt a message with Raja's public key and decrypt with his private key (asymmetric encryption).

**Commands**:  
 1. Raja generate his RSA private key and extract his public key
 ```bash
openssl genpkey -algorithm RSA -out raja_private.pem -pkeyopt rsa_keygen_bits:2048
```

```bash
openssl rsa -pubout -in raja_private.pem -out raja_public.pem
```

 Here for [details](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%203/screenshots/createkeyrsa.png).

2. Danish create secret message
```bash
echo "This is a private message for Danish from Raja." > rahsia.txt
```

![alt text](<screenshots/rahsia.jpg>)

3. Encrypt with Raja's public key
```bash
openssl rsautl -encrypt -inkey danish_public.pem -pubin -in rahsia.txt -out encrypted.bin
```

![alt text](<screenshots/encrypted_rsa.jpg>)

4. Raja decrypt with his private key:
```bash
openssl rsautl -decrypt -inkey raja_private.pem -in rahsia.enc -out rahsia_decrypted.txt
```
Details [here](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%203/screenshots/rsadecrypt.png)

**Result Analysis:**
RSA solves the key distribution problem — Danish can encrypt with Raja’s public key and only Raja can decrypt it with his private key.

