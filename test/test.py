import hashlib

h = hashlib.new("sha256","12345678")
print("Test")
print(h.hexdigest())