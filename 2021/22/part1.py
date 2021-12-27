inp = open("input.txt")

cubes = []
for i in inp:
    i = i.strip()
    i = i.replace('=',' ')
    i = i.replace(',',' ')
    i = i.replace('..',' ')
    i = i.split()
    if abs(int(i[2])) <= 50 and abs(int(i[3])) <= 50:
        cubes.append([i[0], int(i[2]), int(i[3]), int(i[5]), int(i[6]), int(i[8]), int(i[9])])

total = 0
prev = []

def check(i):
    print(i)
    global total, prev
    add = True
    for j in prev:
        if i[0] >= j[0] and i[1] <= j[1] and i[2] >= j[2] and i[3] <= j[3] and i[4] >= j[4] and i[5] <= j[5]:
            return
        if i[0] < j[0] and i[1] >= j[0]:
            add = False
            check([i[0], j[0] - 1] + i[2:])
        if i[1] > j[1] and i[0] <= j[1]:
            add = False
            check([j[1] + 1] + i[1:])
        if i[2] < j[2] and i[3] >= j[2]:
            add = False
            check(i[:2] + [i[2], j[2] - 1] + i[4:])
        if i[3] > j[3] and i[2] <= j[3]:
            add = False
            check(i[:2] + [j[3] + 1] + i[3:])
        if i[4] < j[4] and i[5] >= j[4]:
            add = False
            check(i[:5] + [j[4] - 1])
        if i[5] > j[5] and i[4] <= j[5]:
            add = False
            check(i[:4] + [j[5] + 1, i[5]])
        if not add:
            return
    prev.append(i)
    print(prev)
    print((i[1] - i[0] + 1) * (i[3] - i[2] + 1) * (i[5] - i[4] + 1))
    total += (i[1] - i[0] + 1) * (i[3] - i[2] + 1) * (i[5] - i[4] + 1)

for i in cubes[::-1]:
    if i[0] == "on":
        check(i[1:])
    else:
        prev.append(i[1:])
        print(i)
        print(prev)

print(total)

# part 1:
