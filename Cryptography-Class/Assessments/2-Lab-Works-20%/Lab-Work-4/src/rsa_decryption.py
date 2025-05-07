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