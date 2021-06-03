from functools import reduce

input = 34000000

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

y = 1
while True:
    presents = sum(factors(y))

    if presents * 10 > input:
        print(y)
        break
    y += 1

# part 1: 786240