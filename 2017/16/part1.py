input = open("input.txt")
input = input.readline()
input = input.split(",")

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

for i in input:
    if i[0] == "s":
        index = len(programs) - int(i[1:])
        programs = programs[index:] + programs[:index]
    else:
        swap = i[1:].split("/")
        if i[0] == "x":
            swapi = [int(swap[0]), int(swap[1])]
        elif i[0] == "p":
            swapi = [programs.index(swap[0]), programs.index(swap[1])]
        programs.insert(min(swapi), programs.pop(max(swapi)))
        s = programs.pop(min(swapi) + 1)
        programs.insert(max(swapi), s)

print("".join(programs))

# part 1: olgejankfhbmpidc
