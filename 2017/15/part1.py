a = 634
b = 301
fa = 16807
fb = 48271
r = 2147483647

count = 0
for i in range(40000000):
    a = (a * fa) % r
    b = (b * fb) % r
    if bin(a)[-16:] == bin(b)[-16:]:
        count += 1

print(count)

# part 1: 573
