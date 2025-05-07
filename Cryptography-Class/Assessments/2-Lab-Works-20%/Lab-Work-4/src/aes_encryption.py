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