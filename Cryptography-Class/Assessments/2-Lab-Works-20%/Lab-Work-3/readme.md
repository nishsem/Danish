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

**Tools Used:**
- `OpenSSL` (command line)
- Linux shell utilities (`echo`, `cat`, `diff`)
- `Google Drive` (for sending files to each other)

### Task 1: Symmetric Encryption and Decryption using AES-256-CBC
**Scenario:** Danish wants to send a confidential message to Raja using symmetric encryption.

**Goal:** Encrypt a message using a shared key (symmetric encryption) and then decrypt it with the same key.

**Commands:**
1. Danish generate a strong random key
```bash
openssl rand -hex 32 > key.bin
```
> `rand -hex 32`: Generates 32 random bytes in hex (256 bits) — used as AES key.
<details>
<summary>Screenshots</summary>
<br>

![alt text](<screenshots/generate_key.jpg>)

![alt text](<screenshots/key.jpg>)
</details>

---

2. Create a plaintext message
```bash
echo "Hello, this is a secret message from Danish." > message.txt
```

<details>
<summary>Screenshot</summary>
<br>

![alt text](<screenshots/message.jpg>)
</details>

---

3. Danish encrypt using AES-256-CBC
```bash
openssl enc -aes-256-cbc -salt -in message.txt -out encrypted_message.bin -pass file:./key.bin
```
> - `enc` : Encryption utility.

> - `aes-256-cbc` : Specifies AES with 256-bit key in CBC mode.

> - `salt` : Adds salt to prevent dictionary attacks.

> - `pass file` : ./key.bin: Reads key from file.
<details>
<summary>Screenshot</summary>
<br>

![alt text](<screenshots/aes_enctrypted.jpg>)
</details>

---

4. Raja got the fle from Danish and decrypt it back
```bash
openssl enc -aes-256-cbc -d -in encrypted_message.bin -out mesejrahsia.txt -pass file:$PWD/key.bin
```
> - `d` : Decrypt mode.

> - Output should match the original.

5. See how Raja verify [here](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%203/readme.md#commands-executed)

**Result Analysis:**
- The original and decrypted files are identical, demonstrating that symmetric encryption with AES-256-CBC using a strong random key works as expected.

- This demonstrates how symmetric encryption works using AES-256. Both sender and receiver need the same secret key, which makes key distribution tricky in real life.

> Security Note: CBC mode is vulnerable to certain attacks. For production, use authenticated modes like GCM

### Task 2: Asymmetric Encryption and Decryption using RSA
**Scenario:** Raja wants to securely receive messages from Danish using RSA public-key cryptography.

**Goal:** Use RSA to encrypt a message with Raja's public key and decrypt with his private key (asymmetric encryption).

**Commands:**:  
 1. Raja generate his RSA private key and extract his public key
 ```bash
openssl genpkey -algorithm RSA -out raja_private.pem -pkeyopt rsa_keygen_bits:2048
```
> - `openssl` : Calling the OpenSSL tool.

> - `genpkey` : Stands for "generate private key".

> - `-algorithm RSA` : Specifies the algorithm to use – in this case, RSA..

> - `-out raja_private.pem` : Tells OpenSSL to save the generated private key into raja_private.pem.

> - `-pkeyopt rsa_keygen_bits:2048` : Sets the key size to 2048 bits, which is a strong and secure length for RSA.

```bash
openssl rsa -pubout -in raja_private.pem -out raja_public.pem
```
> - `openssl rsa` : Tells OpenSSL you're working with an RSA key.

> - `-pubout` : Instructs OpenSSL to output the public key.

> - `-in raja_private.pem` : Specifies the input file, which is the private key.

> - `-out raja_public.pem` : Specifies the output file for the public key.

 Here for [details](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%203/readme.md#commands-executed-1).

2. Danish create secret message
```bash
echo "This is a private message for Danish from Raja." > rahsia.txt
```

<details>
<summary>Screenshot</summary>
<br>

![alt text](<screenshots/aes_enctrypted.jpg>)
</details>

---

3. Encrypt with Raja's public key
```bash
openssl rsautl -encrypt -inkey raja_public.pem -pubin -in rahsia.txt -out encrypted.bin
```
> - `openssl rsautl` : Uses the RSA utility tool.

> - `-encrypt` : Tells OpenSSL to perform encryption.

> - `-inkey raja_public.pem` : Specifies the public key file used to encrypt the data.

> - `-pubin	` : Tells OpenSSL that the input key (-inkey) is a public key.

> - `-in rahsia.txt` : The plaintext input file you want to encrypt.

> - `-out encrypted.bin` : The output file where the encrypted data will be stored.

<details>
<summary>Screenshot</summary>
<br>

![alt text](<screenshots/encrypted_rsa.jpg>)
</details>

---

4. Raja decrypt with his private key:
```bash
openssl rsautl -decrypt -inkey raja_private.pem -in rahsia.enc -out rahsia_decrypted.txt
```
> - `-decrypt` : Tells OpenSSL to perform decryption using the private key.

> - `-inkey raja_private.pem` : Specifies the private key file (raja_private.pem) to be used for decryption.

> - `-out rahsia_decrypted.txt` : Specifies the output file (rahsia_decrypted.txt) where the decrypted data will be saved.

Details [here](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%203/readme.md#commands-executed-1).

**Result Analysis:**
- RSA solves the key distribution problem because Danish can encrypt with Raja’s public key and only Raja can decrypt it with his private key.

- The decrypted message matches the original, confirming correct use of RSA for secure communication.

> Security Note: RSA is computationally expensive and not suitable for large files.

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
> - `dgst` : Stands for "digest," which is used for generating cryptographic hash values.

> - `-sha256` : Specifies the hash algorithm to use – in this case, SHA-256.

> - `integrity.txt` : The input file (integrity.txt) for which the SHA-256 hash will be calculated.

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

<details>
<summary>Screenshot</summary>
<br>

![alt text](<screenshots/integrity.jpg>)
**Different output, hash changed.**
</details>

---

**Result Analysis:**
Even a 1-character change causes a completely different hash. This proves that hashing helps verify data integrity.

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
> - `dgst` : -sha256: Hashing before signing.

> - `-sign raja_private.pem` :  Signs the hash of the agreement.txt file using the private key stored in raja_private.pem.

> - `-out agreement.sig` :  Specifies the output file (agreement.sig) where the signature will be saved.

> - `agreement.txt` : The input file whose hash will be signed with the private key

More details [here](https://github.com/Ha1qal/Raja-Haiqal/blob/master/Cryptography-Class/Assessments/Lab%20Works/Lab%203/readme.md#commands-executed-3)

3. Raja share the agreement and signature with Danish and Danish verifies using Raja’s public key
```bash
openssl dgst -sha256 -verify raja_public.pem -signature agreement.sig agreement.txt
```

Output:
```mathematica
Verified OK
```

<details>
<summary>Screenshot</summary>
<br>

![alt text](<screenshots/verify.jpg>)
**Verified OK → file is authentic & untampered.**
</details>

---

4. Danish modify the agreement and he verify again
```bash
echo " Altered." >> agreement.txt
```

```bash
openssl dgst -sha256 -verify raja_public.pem -signature agreement.sig agreement.txt
```
Output:
```mathematica
Verification Failure
```

<details>
<summary>Screenshot</summary>
<br>

![alt text](<screenshots/fail.jpg>)
**You'll see "Verification Failure" because the document has changed, but the signature was created for the original document**
</details>

---

**Result Analysis:**  
Digital signatures confirm:
- The file is from Raja (authenticity)

- The file hasn’t been changed (integrity)

This demonstrates how digital signatures ensure both authentication (it was signed by the private key holder) and integrity (the document hasn't changed since signing). These cryptographic operations form the foundation of modern secure communications and data protection systems.

> Security Note: Digital signatures are crucial for non-repudiation and tamper detection

### Problems Encountered & Troubleshooting
| Problem Type            | Issue Description                                                | How It Was Resolved                    |
|-------------------------|------------------------------------------------------------------|----------------------------------------|
| Command Syntax Errors   | Misplaced flags like `-in` vs. `-inkey` causing execution issues | Used `man openssl`, Google searches, and Stack Overflow to find correct syntax |
| File Not Found Errors   | Errors due to incorrect or missing file paths                    | Double-checked file locations and ensured correct filenames were used             |
| Parameter Understanding | Confused between `-pass` and `-passin`                           | Read the official OpenSSL documentation and followed community tutorials             |

### Summary of Findings
* Symmetric encryption (AES-256-CBC) is fast and suitable for large data, but key management is critical.

* Asymmetric encryption (RSA) is ideal for secure key exchange and small data but not efficient for large files.

* Hashing (SHA-256) provides strong integrity checks because even minor changes in data result in drastically different hashes.

* Digital signatures combine hashing and asymmetric encryption to ensure authenticity and integrity.

* Concepts clarified: AES vs RSA, hashing vs encryption, signing vs verifying

* Troubleshooting relied on OpenSSL documentation, man pages, and community forums also AI :) .