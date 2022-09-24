import hashlib

result = "password"

for i in range(50):
    result = hashlib.md5(result.encode('utf-8'))
    result = result.hexdigest()[:-16]
    print(result)
