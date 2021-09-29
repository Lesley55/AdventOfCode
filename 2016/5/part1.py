import hashlib

input = "ffykfhsq"
id = 0
password = ""

while True:
    door = input + str(id)
    result = hashlib.md5(door.encode())
    hex = result.hexdigest()
    if hex[0:5] == "00000":
        password += str(hex[5:6])

    if len(password) >= 8:
        break
    id += 1

print(password)

# part 1: c6697b55