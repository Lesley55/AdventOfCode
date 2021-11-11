input = open("input.txt")

x = 2
y = 2
code = ""

for i in input:
    for j in i:
        if j == "U":
            y-=1
        elif j == "D":
            y+=1
        elif j == "R":
            x+=1
        elif j == "L":
            x-=1
        
        if x < 1:
            x = 1
        if x > 3:
            x = 3
        if y < 1:
            y = 1
        if y > 3:
            y = 3
    code += str((y-1)*3+x) # x y
print(code)

# part 1: 36961 to low