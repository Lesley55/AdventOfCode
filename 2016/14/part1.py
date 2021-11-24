import hashlib

input = "qzyelonm"
input = "abc"
index = 0
found = 0


def hash(str2hash):
    result = hashlib.md5(str2hash.encode())
    return result.hexdigest().lower()


def next1000(r):
    for j in range(1000):
        result2 = hash(input + str(index + 1 + j))
        for k in range(len(result2)-4):
            if r == result2[k] and r == result2[k+1] and r == result2[k+2] and r == result2[k+3] and r == result2[k+4]:
                print(index, found)
                # print(result2)
                return True
    return False


def check(result):
    global found
    for i in range(len(result)-2):
        r = result[i]
        if r == result[i+1] and r == result[i+2]:
            if next1000(r):
                # print(result)
                found += 1
                return


# while found < 64:
while found < 68:
    result = hash(input + str(index))
    check(result)
    index += 1

print(index-1)

# part 1: 15168 but in wrong place index 66 and example at index 67
