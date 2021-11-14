input = open("input.txt")

def decompress(i):
    length = 0
    start = None

    j = 0
    while j < len(i):
        if i[j] == "(":
            start = j
        elif i[j] == ")" and start is not None:
            par = i[start+1:j]
            par = par.split('x')

            length += int(par[1]) * decompress(i[j+1:j+1+int(par[0])])

            j += int(par[0])
            start = None
        elif start is None:
            length += 1
        
        j += 1    
    
    return length


for i in input: # only 1 line
    print(decompress(i))

# part 2: 11658395076
