## Task 1: Generate Your GPG Key Pair

Objective: Use `gpg` to generate an RSA key pair tied to your identity.

**Step 1: Generate RSA Key Pair**
```bash
gpg --full-generate-key
```
![alt text](screenshots/generate_key.png)

When prompted, I entered the following:

Key Type: RSA and RSA (option 1)

Key Size: 4096 bits

Key Expiry: 1y (1 year)

Name: Ahmad Danish Haikal

Email: adanish.abdullah@student.gmi.edu.my

Passphrase: [entered securely]

```bash
┌──(nish㉿NWS23010014)-[~]
└─$ gpg --full-generate-key
gpg (GnuPG) 2.2.46; Copyright (C) 2024 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: keybox '/home/danish/.gnupg/pubring.kbx' created
Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
  (14) Existing key from card
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) y
invalid value
Key is valid for? (0) 1y
Key expires at Sat 16 May 2026 06:26:53 PM +08
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: Ahmad Danish Haikal
Email address: adanish.abdullah@student.gmi.edu.my
Comment: Practical Test 1
You selected this USER-ID:
    "Ahmad Danish Haikal (Practical Test 1) <adanish.abdullah@student.gmi.edu.my>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: /home/danish/.gnupg/trustdb.gpg: trustdb created
gpg: directory '/home/danish/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/home/danish/.gnupg/openpgp-revocs.d/862235543AA4ECCCDF3ADC20C350E84E8CAFF6CB.rev'
public and secret key created and signed.

pub   rsa4096 2025-05-16 [SC] [expires: 2026-05-16]
      862235543AA4ECCCDF3ADC20C350E84E8CAFF6CB
uid                      Ahmad Danish Haikal (Practical Test 1) <adanish.abdullah@student.gmi.edu.my>
sub   rsa4096 2025-05-16 [E] [expires: 2026-05-16]
```

**Step 2: List the Generated Key**
```bash
gpg --list-keys
```

![alt text](screenshots/list_keys.png)

**GPG key pair was successfully generated and linked to my identity.**

## Task 2: Encrypt and Decrypt Files Using GPG

Objective: Use GPG to encrypt and decrypt a file using the public and private key pair you created in Task 1.

**Step 1: Create a Test File**
```bash
echo "This file was encrypted by Nish (NWS23010014)" > message.txt
```
