least = 99999999999

def next(bossHitPoints, playerHitPoints, mana, spend, shield, poison, recharge, turn):
    global least
    bossDamage = 8

    if playerHitPoints <= 0 or spend >= least:
        return
    elif bossHitPoints <= 0:
        if spend < least:
            least = spend
        return

    if shield > 0:
        shield -= 1
    if poison > 0:
        bossHitPoints -= 3
        poison -= 1
    if recharge > 0:
        mana += 101
        recharge -= 1
    
    if turn % 2 == 0:
        turn += 1
        if mana < 53:
            return
        if mana >= 53:
            b = bossHitPoints - 4
            m = mana - 53
            s = spend + 53
            next(b, playerHitPoints, m, s, shield, poison, recharge, turn)
        if mana >= 73:
            b = bossHitPoints - 2
            p = playerHitPoints + 2
            m = mana - 73
            s = spend + 73
            next(b, p, m, s, shield, poison, recharge, turn)
        if mana >= 113:
            sh = shield + 6
            m = mana - 113
            s = spend + 113
            next(bossHitPoints, playerHitPoints, m, s, sh, poison, recharge, turn)
        if mana >= 173:
            p = poison + 6
            m = mana - 173
            s = spend + 173
            next(bossHitPoints, playerHitPoints, m, s, shield, p, recharge, turn)
        if mana >= 229:
            r = recharge + 5
            m = mana - 229
            s = spend + 229
            next(bossHitPoints, playerHitPoints, m, s, shield, poison, r, turn)
    else:
        turn += 1
        diff = bossDamage
        if shield > 0:
            diff -= 7
        if diff < 1:
            diff = 1
        playerHitPoints -= diff
        next(bossHitPoints, playerHitPoints, mana, spend, shield, poison, recharge, turn)

next(55, 50, 500, 0, 0, 0, 0, 0)
print(least)

# part 1: 953