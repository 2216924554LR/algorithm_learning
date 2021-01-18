import hashlib

s = "hello world!"
s = s.encode(encoding='UTF-8')

myHash1 = hashlib.md5(s).hexdigest()

myHash2 = hashlib.sha1(s).hexdigest()

print(myHash1)
print(myHash2)