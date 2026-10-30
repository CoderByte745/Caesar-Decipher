msg = input("Enter msg: ")
key = int(input("key: "))
new = ""
for i in range(len(msg)):
    new += chr((94 + (ord(msg[i]) + key)-32)%94+32)
print(new)