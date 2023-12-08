input = open("input.txt")
input = input.readlines()

lr = input[0]
ins = {}
for i in input[2:]:
    i = i.replace("(", "").replace(")", "").replace(",", "").split()
    ins[i[0]] = (i[2], i[3])

pos = []
for i in ins.keys():
    if i[2] == "A":
        pos.append(i)

steps = 0
l = len(lr) - 1

end = False
z = {}
while not end:
    for i in range(len(pos)):
        if lr[steps % l] == "L":
            pos[i] = ins[pos[i]][0]
        else:
            pos[i] = ins[pos[i]][1]
    steps += 1
    # save steps if pos contains z
    for i in range(len(pos)):
        if pos[i][2] == "Z":
            if not i in z:
                z[i] = [(pos[i], steps)]
    # after string + z it becomes same string + z, no other strings containing z in between
    # getting difference isnt nessesary because its the same as from start to first found, so finding 1 is enough
    if len(z) == len(pos):
        end = True

a = []
for i in z:
    a.append(z[i][0][1])

big = a[-1]
s = a[-1]
d = True
while d:
    s += big
    d = False
    for i in a[:-1]:
        if s % i != 0:
            d = True
            break

print(s)

# part 2: 20220305520997 
# takes a few minutes, but works
# could probably improve using chinese reststelling
