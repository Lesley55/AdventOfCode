input = open("input.txt")

discs = []

for i in input:
    a = i.replace('.', '').split()
    discs.append([int(a[3]), int(a[11])])

discs.append([11, 0])

time = 0

def check():
    for i in range(len(discs)):
        if (discs[i][1] + time + i) % discs[i][0] == 0:
            continue
        else:
            return False
    return True

while True:
    time += 1
    if check():
        print(time-1)
        break

# part 2: 2408135
