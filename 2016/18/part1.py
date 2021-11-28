input = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."

rows = 40

totalSafe = 0

for i in range(rows):
    totalSafe += input.count(".")
    print(input)
    
    new = ""
    for j in range(len(input)):
        a = ""
        if j == 0:
            a = "." + input[j:j+2]
        elif j == len(input)-1:
            a = input[j-1:j+1] + "."
        else:
            a = input[j-1:j+2]
        
        if a == "^^." or a == ".^^" or a == "^.." or a == "..^":
            new += "^"
        else:
            new += "."
    input = new

print(totalSafe)

# part 1: 2013
