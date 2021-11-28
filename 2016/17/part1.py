import hashlib

passcode = "hhhxzeay"

open = "bcdef"
possible = [[0,0,passcode]]

def nextDoor(x, y, input):
    if x < 0 or y < 0 or 4 <= x or 4 <= y:
        return False
    elif x == 3 and y == 3:
        return True

    result = hashlib.md5(input.encode())
    hex = result.hexdigest()
    four = hex[0:4]

    for i in range(len(four)):
        if four[i] in open:
            if i == 0:
                possible.append([x, y - 1, input + "U"])
            elif i == 1:
                possible.append([x, y + 1, input + "D"])
            elif i == 2:
                possible.append([x - 1, y, input + "L"])
            elif i == 3:
                possible.append([x + 1, y, input + "R"])

for i in possible:
    if nextDoor(i[0], i[1], i[2]):
        print(i[2])
        break

# part 1: DDRUDLRRRD
