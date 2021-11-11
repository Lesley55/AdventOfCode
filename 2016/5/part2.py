import hashlib

input = "ffykfhsq"
id = 0
password = "--------"

while True:
    door = input + str(id)
    result = hashlib.md5(door.encode())
    hex = result.hexdigest()
    if hex[0:5] == "00000":
        place = hex[5:6]
        if place.isdigit():
            place = int(place)
            char = str(hex[6:7])
            if place < 8:
                if password[place:place+1] == "-":
                    password = password[:place] + char + password[place+1:]
    
    if not "-" in password:
        break
    id += 1

print(password)

# part 2: 8c35d1ab