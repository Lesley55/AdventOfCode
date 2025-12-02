input = open("input.txt")
input = input.readline().split(",")

total = 0

for i in input:
    i = i.split("-")
    for j in range(int(i[0]), int(i[1]) + 1):
        k = str(j)
        l = int(len(k) / 2)
        if k[:l] == k[l:]:
            total += j

print(total)

# part 1: 40055209690
