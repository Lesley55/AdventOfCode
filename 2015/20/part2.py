from functools import reduce

input = 34000000

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

elf = {}

y = 1
while True:
    presents = 0

    f = factors(y)
    for ff in f:
        if ff in elf:
            if not elf[ff] >= 50:
                presents += ff
        else: 
            presents += ff
        if ff in elf:
            elf[ff] += 1
        else:
            elf[ff] = 1

    if presents * 11 > input:
        print(y)
        break
    y += 1

# part 2: 831600