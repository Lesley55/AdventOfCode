input = open("input.txt")
input = input.readline()

total = 0
opened = ""
i = 0
while i < len(input):
    if input[i] == "!":
        i += 2
        continue
    elif 0 < len(opened) and opened[-1] == "<":
        if input[i] == ">":
            opened = opened[:-1]
    elif input[i] == "{" or input[i] == "<":
        opened += input[i]
    elif input[i] == "}":
        total += len(opened)
        opened = opened[:-1]
    i += 1

print(total)

# part 1: 16689
