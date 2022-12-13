from ast import literal_eval

input = open("input.txt")

packets = []
for i in input:
    i = i.strip()
    if i == "":
        continue
    i = literal_eval(i)
    packets.append(i)

def compare(a, b):
    for i in range(len(a)):
        if i >= len(b):
            return False
        elif type(a[i]) == int and type(b[i]) == int:
            if a[i] > b[i]:
                return False
            elif a[i] < b[i]:
                return True
        elif type(a[i]) == list and type(b[i]) == list:
            c = compare(a[i], b[i])
            if c != None:
                return c
        elif type(a[i]) == int and type(b[i]) == list:
            c = compare([a[i]], b[i])
            if c != None:
                return c
        elif type(a[i]) == list and type(b[i]) == int:
            c = compare(a[i], [b[i]])
            if c != None:
                return c
    if len(b) > len(a):
        return True
    return None

indices = []
for i in range(0, len(packets), 2):
    a = packets[i]
    b = packets[i + 1]
    if compare(a, b):
        indices.append(int(i / 2) + 1)

print(sum(indices))
# part 1: 5350
