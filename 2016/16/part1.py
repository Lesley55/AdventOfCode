input = "11101000110010100"
disk = 272

while len(input) < disk:
    reverse = input[::-1]
    new = ""
    for i in reverse:
        if i == "0":
            new += "1"
        else:
            new += "0"
    input += "0" + new

checksum = input[:disk]

while len(checksum) % 2 == 0:
    newsum = ""
    for i in range(0, len(checksum), 2):
        if checksum[i] == checksum[i + 1]:
            newsum += "1"
        else:
            newsum += "0"
    checksum = newsum

print(checksum)

# part 1: 10100101010101101
