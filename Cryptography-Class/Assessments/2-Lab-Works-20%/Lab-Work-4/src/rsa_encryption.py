from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# 1. Import Raja's public key (paste it here)
public_key_str = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1JqRbGfSKHggm4rllcd7
WnsCa4Pm7y4/4xw01+pNI3gtWXOvLX3xU3E9CdQzU8U7rFG3e8on4D7CleQdDclW
am92Qn4wcC16oWqwhwrWP3+krvYjKEFx7pMMvvg/Jc/shnyjugNogyN7guhtMsdf
UDOsxOsk4GN/1iW0oOfrNnm7DrhWMa6yL9lKIjnLr96jZOUSRl7+tld5nRwvsDmL
cgl5oGM+KMWi6hcsn/lvzGz+i53j74oaI9uAMRtfd5bvaRg6vjUQQun9gp1CdJ0h
o3+qWDWZqcE0ew7xCpO40sbVwY2B3Y7XAFAp81vPLFalnGVBa70SP7tMVvRDRimJ
0wIDAQAB
-----END PUBLIC KEY-----'''

public_key = RSA.import_key(public_key_str)

# 2. Create RSA cipher
cipher_rsa = PKCS1_OAEP.new(public_key)

# 3. Encrypt message
message = b"This message is for Raja!"
ciphertext = cipher_rsa.encrypt(message)

# 4. Encode ciphertext
print("Encrypted:", base64.b64encode(ciphertext).decode())