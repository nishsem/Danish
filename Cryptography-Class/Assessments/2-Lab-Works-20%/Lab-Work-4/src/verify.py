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