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
find("000000")

# part 1: 346386
# part 2: 

# takes to long
# there is probably a better/optimized way to do this, where you just look what starting value produces the zero's, 
# so you don't have to check every number, but i don't know how the algoritm works