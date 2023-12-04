input = open("input.txt")

cards = []
for i in input:
    cards.append(1)

input.close()
input = open("input.txt")

card = 0
for i in input:
    i = i.replace("/n", "").split()
    winning = i[2:12]
    numbers = i[13:]
    wins = 0
    for n in numbers:
        if n in winning:
            wins += 1
    for w in range(wins):
        cards[card + 1 + w] += cards[card]
    card += 1

print(sum(cards))

# part 2: 5667240
