a = 634
b = 301
fa = 16807
fb = 48271
r = 2147483647

pairs = 0
count = 0
valuesA = []
valuesB = []
while True:
    if len(valuesA) > 0 and len(valuesB) > 0:
        pairs += 1
        pa = valuesA[0]
        pb = valuesB[0]
        valuesA = valuesA[1:]
        valuesB = valuesB[1:]
        if bin(pa)[-16:] == bin(pb)[-16:]:
            count += 1
    if pairs >= 5000000:
        break
    if len(valuesA) == 0:
        a = (a * fa) % r
        if a % 4 == 0:
            valuesA.append(a)
    if len(valuesB) == 0:
        b = (b * fb) % r
        if b % 8 == 0:
            valuesB.append(b)

print(count)

# part 2: 294
