import hashlib

input = "iwrupvqb"

def find(zero):
    number = 1

    while True:
        s = input + str(number)
        result = hashlib.md5(s.encode())
        hex = result.hexdigest()

        if hex[0:6] == zero:
            print(number)
            break

        number += 1

find("000000")

# part 2: 9958218