input = open("input.txt")

oxygen = []
scrubber = []
for i in input:
    oxygen.append(i.strip())
    scrubber.append(i.strip())

oxbits = []
def countox():
    global oxbits
    for i in range(len(oxbits)):
        oxbits[i] = 0
    for i in oxygen:
        for j in range(len(i)):
            if i[j] == "1":
                if j < len(oxbits):
                    oxbits[j] += 1
                else:
                    oxbits.append(1)
scrubits = []
def countscrub():
    global scrubits
    for i in range(len(scrubits)):
        scrubits[i] = 0
    for i in scrubber:
        for j in range(len(i)):
            if i[j] == "1":
                if j < len(scrubits):
                    scrubits[j] += 1
                else:
                    scrubits.append(1)

def findLast(a, b, i):
    l = 0
    while l < len(a):
        if a[l][i] != b and len(a) > 1:
            a.pop(a.index(a[l]))
            continue
        l += 1

countox()
for i in range(len(oxbits)):
    if oxbits[i] >= len(oxygen) / 2:
        findLast(oxygen, "1", i)
    else:
        findLast(oxygen, "0", i)
    countox()

countscrub()
for i in range(len(scrubits)):
    if scrubits[i] >= len(scrubber) / 2:
        findLast(scrubber, "0", i)
    else:
        findLast(scrubber, "1", i)
    countscrub()

print(int(oxygen[0], 2) * int(scrubber[0], 2))

# part 2: 4636702
