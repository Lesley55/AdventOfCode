input = open("input.txt")

score = 0
points = {'X': 1, 'Y': 2, 'Z': 3, 'A X': 3, 'A Y': 6, 'A Z': 0, 'B X': 0, 'B Y': 3, 'B Z': 6, 'C X': 6, 'C Y': 0, 'C Z': 3}
for i in input:
    i = i.strip()
    score += points[i]
    shapes = i.split(' ')
    score += points[shapes[1]]

print(score)
# part 1: 12276
