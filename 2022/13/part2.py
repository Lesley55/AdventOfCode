from ast import literal_eval

input = open("input.txt")

packets = []
for i in input:
    i = i.strip()
    if i == "":
        continue
    i = literal_eval(i)
    packets.append(i)

dividers = [[[2]], [[6]]]
packets += dividers

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

ordered = [packets[0]]
for i in range(1, len(packets)):
    t = True
    for j in ordered:
        if not compare(j, packets[i]):
            ordered.insert(ordered.index(j), packets[i])
            t = False
            break
    if t:
        ordered.append(packets[i])

print((ordered.index(dividers[0]) + 1) * (ordered.index(dividers[1]) + 1))
# part 2: 19570
