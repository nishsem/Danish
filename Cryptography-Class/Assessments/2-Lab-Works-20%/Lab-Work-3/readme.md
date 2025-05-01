# Lab 3: Hands-on Exploration of Cryptographic Tools with OpenSSL

## A. Objectives:

This lab introduces to OpenSSL, a widely used cryptography toolkit, for performing essential cryptographic operations such as:

1. Symmetric encryption (AES)
2. Asymmetric encryption (RSA)
3. Hashing (SHA-256)
4. Digital signatures (RSA with SHA-256)

By the end of this lab, we will be able to:

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
1. Danish generate a strong random key
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

![alt text](<screenshots/message.jpg>)

3. Encrypt using AES-256-CBC
```bash
openssl enc -aes-256-cbc -salt -in message.txt -out encrypted_message.bin -pass file:./key.bin
```
> - `enc` : Encryption utility

> - `aes-256-cbc` : Specifies AES with 256-bit key in CBC mode

> - `salt` : Adds salt to prevent dictionary attacks

> - `pass file` : ./key.bin: Reads key from file

![alt text](<screenshots/aes_enctrypted.jpg>)

4. Raja decrypt it back
```bash
openssl enc -aes-256-cbc -d -in encrypted_message.bin -out mesejrahsia.txt -pass file:$PWD/key.bin
```
> - d: Decrypt mode

> - Output should match the original

5. See how Raja verify [here](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%203/screenshots/decrypttask1.png)

### Task 2: Asymmetric Encryption and Decryption using RSA
**Goal:** Use RSA to encrypt a message with Raja's public key and decrypt with his private key (asymmetric encryption).

**Commands:**:  
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
Details [here](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%203/screenshots/rsadecrypt.png).

**Result Analysis:**
RSA solves the key distribution problem because Danish can encrypt with Raja’s public key and only Raja can decrypt it with his private key.

### Task 3: Hashing and Message Integrity using SHA-256
**Goal:** Show how hashes detect any file tampering.

**Commands:**
1. Danish create a file:
```bash
echo "This is an important document from Danish to Raja." > integrity.txt
```

2. Hash it
```bash
openssl dgst -sha256 integrity.txt
```
Output:
> SHA2-256(integrity.txt)= `8aca8c9981a01e58d9031e16f404248014d76daba78d3f89f709b66e3855d07f`

3. Raja Modify the file slightly
```bash
echo " " >> integrity.txt
```

4. Danish hash the original file with the modified file by Raja
```bash
openssl dgst -sha256 integrity.txt integrity1.txt
```
Output:
> SHA2-256(integrity.txt)= `8aca8c9981a01e58d9031e16f404248014d76daba78d3f89f709b66e3855d07f`

> SHA2-256(integrity1.txt)= `e9fec22e3b60289908f0a7785b0356ab3263806df1593be1b2adc85c5d505abd`

![alt text](<screenshots/integrity.jpg>)

Different output, hash changed.

### Task 4: Digital Signatures using RSA
**Goal:** Sign a file with Raja's private key, verify it with Raja's public key to confirming authenticity and integrity.

**Commands:**
1. Raja create a file to sign:
```bash
echo "This agreement confirms the terms between Danish and Raja." > agreement.txt
```

2. Sign using Raja’s private key (from Task 2):
```bash
openssl dgst -sha256 -sign raja_private.pem -out agreement.sig agreement.txt
```
More details [here]()

3. Raja share the agreement and signature with Danish and Danish verifies using Raja’s public key
```bash
openssl dgst -sha256 -verify raja_public.pem -signature agreement.sig agreement.txt
```