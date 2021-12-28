inp = open("input.txt")

cubes = []
for i in inp:
    i = i.strip()
    i = i.replace('=',' ')
    i = i.replace(',',' ')
    i = i.replace('..',' ')
    i = i.split()
    # if abs(int(i[2])) <= 50 and abs(int(i[3])) <= 50: # uncomment for part 1
    cubes.append([i[0], int(i[2]), int(i[3]), int(i[5]), int(i[6]), int(i[8]), int(i[9])])

total = 0
prev = []

def check(i):
    global total, prev
    for j in prev:
        x, y, z = False, False, False
        if i[0] >= j[0] and i[1] <= j[1]:
            x = True
        if i[2] >= j[2] and i[3] <= j[3]:
            y = True
        if i[4] >= j[4] and i[5] <= j[5]:
            z = True
        
        if x and y and z:
            return
        
        p = {"x": [], "y": [], "z": []}
        if i[0] < j[0] and i[1] >= j[0]:
            p["x"].append([i[0], j[0] - 1] + i[2:])
        if i[1] > j[1] and i[0] <= j[1]:
            p["x"].append([j[1] + 1] + i[1:])
        if i[2] < j[2] and i[3] >= j[2]:
            p["y"].append(i[:2] + [i[2], j[2] - 1] + i[4:])
        if i[3] > j[3] and i[2] <= j[3]:
            p["y"].append(i[:2] + [j[3] + 1] + i[3:])
        if i[4] < j[4] and i[5] >= j[4]:
            p["z"].append(i[:5] + [j[4] - 1])
        if i[5] > j[5] and i[4] <= j[5]:
            p["z"].append(i[:4] + [j[5] + 1, i[5]])
        
        if (x and len(p["y"]) != 0 and len(p["z"]) != 0) or (y and len(p["x"]) != 0 and len(p["z"]) != 0) or (z and len(p["x"]) != 0 and len(p["y"]) != 0):
            pass
        elif (x and y and len(p["z"]) != 0) or (y and z and len(p["x"]) != 0) or (x and z and len(p["y"]) != 0):
            pass
        elif (len(p["x"]) == 0 or len(p["y"]) == 0 or len(p["z"]) == 0):
            continue

        for k in p:
            for l in p[k]:
                check(l)
        return
    
    prev.append(i)
    total += (i[1] - i[0] + 1) * (i[3] - i[2] + 1) * (i[5] - i[4] + 1)

prevSize = 1
for i in cubes[::-1]:
    if i[0] == "on":
        check(i[1:])
        prev = prev[:prevSize]
        prev.append(i[1:])
    else:
        prev.append(i[1:])
    prevSize += 1

print(total)

# part 1: 655005
# part 2: 1125649856443608
