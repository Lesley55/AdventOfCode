input = open("input.txt")
input = input.readlines()

acc = []
for i in range(len(input)):
    a = input[i].split(", ")
    b = a[2].strip()[3:-1].split(",")
    c = sum(abs(int(x)) for x in b)
    acc.append([i, c])

acc.sort(key=lambda x: x[1])
print(acc[0][0])

# part 1: 376
