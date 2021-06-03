input = 34000000

i = 1
while True:
    presents = 0
    k = 1
    while k <= i:
        if i % k == 0:
            presents += k * 10
        k += 1
    if presents > input:
        print(i)
        break
    i += 1