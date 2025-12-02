input = open("input.txt")
input = input.readline().split(",")

total = 0

for i in input:
    i = i.split("-")
    for j in range(int(i[0]), int(i[1]) + 1):
        k = str(j)
        lk = len(k)
        for m in range(int(lk / 2)):
            if int(len(k)) % (m + 1) == 0:
                s = True
                for n in range(m + 1, lk, m + 1):
                    if k[:m+1] != k[n:n+m+1]:
                        s = False
                        break
                if s:
                    total += j
                    break

print(total)

# part 2: 50857215650
