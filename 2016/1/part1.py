input = open("input.txt")

input = input.read()
input = input.split(', ')

direction = 0
x = 0
y = 0
visited = []
twice = False

for i in input:
    if i[0] == "R":
        direction += 1
        if direction > 3:
            direction = 0
    elif i[0] == "L":
        direction -= 1
        if direction < 0:
            direction = 3

    for n in range(int(i[1:])):
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1

        if not twice:
            if (x, y) in visited:
                print("part 2:" + str(abs(x)+abs(y)))
                twice = True
            else:
                visited.append((x, y))

print("part 1:" + str(abs(x)+abs(y)))

# part 1: 209
# part 2: 136




# def faculteit(i, j=1):
#     if i <= 0:
#         print(j)
#         return
#     faculteit(i-1, j*i)

# faculteit(5)
