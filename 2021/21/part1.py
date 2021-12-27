player1 = 1 - 1
player2 = 2 - 1
score1 = 0
score2 = 0

dice = 0
while True:
    for i in range(3):
        player1 += dice % 100 + 1
        dice += 1
    score1 += player1 % 10 + 1
    if score1 >= 1000:
        print(dice * score2)
        break
    for i in range(3):
        player2 += dice % 100 + 1
        dice += 1
    score2 += player2 % 10 + 1
    if score2 >= 1000:
        print(dice * score1)
        break

# part 1: 598416