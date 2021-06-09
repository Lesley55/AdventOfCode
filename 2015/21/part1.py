weapons = [[0, 0, 0], [8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armor = [[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [104, 0, 5]]
rings = [[0, 0, 0], [0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

min = 999999999
for w in weapons:
    for a in armor:
        for r in rings:
            for r2 in rings:
                if r != r2:
                    gold = 0

                    bossHitPoints = 104
                    bossDamage = 8
                    bossArmor = 1

                    playerHitPoints = 100
                    playerDamage = 0
                    playerArmor = 0

                    opt = [w, a, r, r2]
                    for o in opt:
                        gold += o[0]
                        playerDamage += o[1]
                        playerArmor += o[2]
                    
                    i = 0
                    while True:
                        if i % 2 == 0:
                            diff = playerDamage - bossArmor
                            if diff < 1:
                                diff = 1
                            bossHitPoints -= diff
                        else:
                            diff = bossDamage - playerArmor
                            if diff < 1:
                                diff = 1
                            playerHitPoints -= diff
                        
                        if playerHitPoints <= 0:
                            break
                        elif bossHitPoints <= 0:
                            if gold < min:
                                min = gold
                            break
                        i += 1

print(min)

# part 1: 78