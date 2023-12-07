input = open("input.txt")
input = input.readlines()
input = [i.split() for i in input]

def score(hand):
    score = 0

    distinct = "".join(set(hand))
    s = sorted(hand)
    if len(distinct) == 1: # five of a kind
        score = 6
    elif len(distinct) == 2:
        if s[0] == s[3] or s[1] == s[4]: # four of a kind
            score = 5
        else: # full house
            score = 4
    elif len(distinct) == 3:
        if s[0] == s[2] or s[1] == s[3] or s[2] == s[4]: # three of a kind
            score = 3
        else: # two pair
            score = 2
    elif len(distinct) == 4: # one pair
        score = 1

    score *= 100 ** 5

    # score per card
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1]
    for card in range(len(hand)):
        score += cards.index(hand[card]) * (100 ** (len(hand) - 1 - card))
    return score

total = 0
input = sorted(input, key=lambda hand: score(hand[0]))
for i in range(len(input)):
    total += (i + 1) * int(input[i][1])

print(total)

# part 1: 254024898
