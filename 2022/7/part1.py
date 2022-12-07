input = open("input.txt")
    
dir = {}
stack = []

def getcurrent():
    current = dir
    for i in stack:
        current = current[i]
    return current

for i in input:
    i = i.strip().split()
    if i[1] == "cd":
        if i[2] == "..":
            stack.pop()
        else:
            if i[2] == "/":
                stack = []
            if not i[2] in getcurrent().keys():
                getcurrent()[i[2]] = {}
            stack.append(i[2])
    elif i[0].isdigit():
        getcurrent()[i[1]] = int(i[0])

def countdir(d):
    global below
    count = 0
    for i in d:
        if isinstance(d[i], int):
            count += d[i]
        else:
            count += countdir(d[i])
    if count <= 100000:
        below += count
    return count
    
below = 0
total = countdir(dir)

# print(total)
print(below)
# part 1: 
