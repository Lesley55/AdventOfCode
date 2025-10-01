input = open("input.txt")
input = input.readlines()

y = 0
x = input[0].index("|")
letters = ""
direction = "S"
directions = {"S": [1,0], "N": [-1,0], "E": [0,1], "W": [0,-1]}

def nextStep(d):
    return [y + directions[d][0], x + directions[d][1]]

def isOutside(y, x):
    return y < 0 or y >= len(input) or x < 0 or x >= len(input[0])

def isPipe(y, x):
    return not isOutside(y, x) and not input[y][x] == " "

steps = 1
while True:
    ny, nx = nextStep(direction)
    if isPipe(ny, nx):
        if input[ny][nx].isalpha():
            letters += input[ny][nx]
    elif input[y][x] == "+":
        for d in ["E", "W"] if direction == "S" or direction == "N" else ["N", "S"]:
            sy, sx = nextStep(d)
            if isPipe(sy, sx):
                direction = d
                continue
        continue
    else:
        break
    y, x = ny, nx
    steps += 1

print("part1: ", letters)
print("part2: ", steps)

# part 1: LIWQYKMRP
# part 2: 16764
