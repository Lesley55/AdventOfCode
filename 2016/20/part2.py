input = open("input.txt")

blacklist = []

for i in input:
    i = i.strip().split("-")
    i = [int(i[0]), int(i[1])]
    blacklist.append(i)

ip = 0

def check():
    global ip
    for i in blacklist:
        if i[0] <= ip and ip <= i[1]:
            ip = i[1] + 1
            return False
    return True

allowed = 0
while ip < 4294967295:
    if check():
        allowed += 1
        ip += 1

print(allowed)

# part 2: 119
