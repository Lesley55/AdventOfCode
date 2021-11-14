input = open("input.txt")

for i in input: # only 1 line

    length = 0
    start = None

    j = 0
    while j < len(i):
        if i[j] == "(":
            start = j
        elif i[j] == ")" and start is not None:
            par = i[start+1:j]
            par = par.split('x')
            length += int(par[0]) * int(par[1])
            j += int(par[0])
            start = None
        elif start is None:
            length += 1
        
        j += 1
    
    print(length)

# part 1: 120765
