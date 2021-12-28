state = {}
def turn(p1, p2, s1, s2, t):
    if (p1, p2, s1, s2, t) in state:
        return state[(p1, p2, s1, s2, t)]
    if s1 >= 21:
        return [1, 0]
    if s2 >= 21:
        return [0, 1]
    wins = [0, 0]
    if t == True:
        for i in [x + y + z for x in range(1,4) for y in range(1,4) for z in range(1,4)]:
            w = turn(p1 + i, p2, s1 + ((p1 + i) % 10 + 1), s2, False)
            wins = [x + y for x, y in zip(wins, w)]
    else:
        for i in [x + y + z for x in range(1,4) for y in range(1,4) for z in range(1,4)]:
            w = turn(p1, p2 + i, s1, s2 + ((p2 + i) % 10 + 1), True)
            wins = [x + y for x, y in zip(wins, w)]
    state[(p1, p2, s1, s2, t)] = wins
    return wins

print(max(turn(1 - 1, 2 - 1, 0, 0, True)))

# part 2: 27674034218179
