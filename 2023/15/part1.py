input = open("input.txt")
input = input.readline().split(",")

total = 0
for i in input:
    h = 0
    for j in i:
        h += ord(j)
        h *= 17
        h %= 256
    total += h

print(total)

# part 1: 512950
