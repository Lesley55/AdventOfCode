input = open("input.txt")

bits = []
length = 0
for i in input:
    length += 1
    for j in range(len(i)):
        if i[j] == "1":
            if j < len(bits):
                bits[j] += 1
            else:
                bits.append(1)

gamma = ""
epsilon = ""
for i in bits:
    if i > length / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))

# part 1: 845186
