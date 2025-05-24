from Crypto.Cipher import AES
from hashlib import sha256
import os

# Rebuild key the same way as the ransomware
KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[:16]  # fix slicing

# Folder paths
enc_folder = "locked_files"
dec_folder = "decrypted"

os.makedirs(dec_folder, exist_ok=True)

# Padding removal
def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# Loop through .enc files and decrypt
for filename in os.listdir(enc_folder):
    if filename.endswith(".enc"):
        enc_path = os.path.join(enc_folder, filename)
        with open(enc_path, "rb") as f:
            ciphertext = f.read()
        
        cipher = AES.new(KEY, AES.MODE_ECB)
        decrypted = cipher.decrypt(ciphertext)
        plaintext = unpad(decrypted)

        # Save to decrypted folder
        new_filename = filename.replace(".enc", "")
        dec_path = os.path.join(dec_folder, new_filename)
        with open(dec_path, "wb") as f:
            f.write(plaintext)

        print(f"[+] Decrypted: {filename} -> {new_filename}")
