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