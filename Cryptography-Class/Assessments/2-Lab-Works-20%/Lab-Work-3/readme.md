# Lab 3: Hands-on Exploration of Cryptographic Tools with OpenSSL

## A. Objectives:

This lab introduces to OpenSSL, a widely used cryptography toolkit, for performing essential cryptographic operations such as:

1. Symmetric encryption (AES)
2. Asymmetric encryption (RSA)
3. Hashing (SHA-256)
4. Digital signatures (RSA with SHA-256)

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
If there's no output, it means both files are identical.

