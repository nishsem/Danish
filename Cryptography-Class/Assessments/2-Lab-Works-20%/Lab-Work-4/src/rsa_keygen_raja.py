from Crypto.PublicKey import RSA

# 1. Generate RSA key pair (2048 bits is standard)
key_pair = RSA.generate(2048)

# 2. Export the private key (keep this secret!)
private_key = key_pair.export_key()
with open("raja_private.pem", "wb") as f:
    f.write(private_key)

# 3. Export the public key (share this with you for encryption)
public_key = key_pair.publickey().export_key()
with open("raja_public.pem", "wb") as f:
    f.write(public_key)

print("RSA key pair generated.")