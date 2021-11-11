import hashlib

input = "iwrupvqb"

def find(zero):
    number = 1

    while True:
        s = input + str(number)
        result = hashlib.md5(s.encode())
        hex = result.hexdigest()

        if hex[0:5] == zero:
            print(number)
            break

        number += 1

find("00000")

# part 1: 346386
