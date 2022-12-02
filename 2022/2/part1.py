input = open("input.txt")

score = 0
score2 = 0
points = {'X': 1, 'Y': 2, 'Z': 3, 'A X': 3, 'A Y': 6, 'A Z': 0, 'B X': 0, 'B Y': 3, 'B Z': 6, 'C X': 6, 'C Y': 0, 'C Z': 3}
points2 = {'X': 0, 'Y': 3, 'Z': 6, 'A X': 3, 'A Y': 1, 'A Z': 2, 'B X': 1, 'B Y': 2, 'B Z': 3, 'C X': 2, 'C Y': 3, 'C Z': 1}
for i in input:
    i = i.strip()
    score += points[i]
    score2 += points2[i]
    shapes = i.split(' ')
    score += points[shapes[1]]
    score2 += points2[shapes[1]]

print(score)
# part 1: 12276
print(score2)
# part 2: 9975
