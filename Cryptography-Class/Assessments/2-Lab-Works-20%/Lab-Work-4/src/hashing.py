import hashlib

# Input data
data1 = "hello"
data2 = "hello world"

# Hash
hash1 = hashlib.sha256(data1.encode()).hexdigest()
hash2 = hashlib.sha256(data2.encode()).hexdigest()

print("Hash of data1:", hash1)
print("Hash of data2:", hash2)