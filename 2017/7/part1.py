input = open("input.txt")

supporting = []
supported = []
for i in input:
    i = i.split("-> ")
    supporting.append(i[0].split()[0])
    if len(i) > 1:
        for j in i[1].replace("\n", "").split(", "):
            supported.append(j)

for s in supporting:
    if not s in supported:
        print(s)
        
# part 1: xegshds
