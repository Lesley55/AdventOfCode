input = open("input.txt")
input = input.readlines()

time = int(input[0].replace(" ", "").split(":")[1])
dist = int(input[1].replace(" ", "").split(":")[1])

ways = 0
for ms in range(time):
    if ms * (time - ms) > dist:
        ways += 1

print(ways)

# part 2: 27102791
