input = open("input.txt")

contains = 0
contains2 = 0
for i in input:
    i = i.strip().split(",")
    a, b, c, d = i[0].split("-") + i[1].split("-")
    a, b, c, d = int(a), int(b), int(c), int(d)
    if((a >= c and b <= d) or (a <= c and b >= d)):
        contains += 1
    if((a >= c and a <= d) or (b <= c and b >= d) or (c >= a and c <= b) or (d <= a and d >= b)):
        contains2 += 1

print(contains)
# part 1: 444
print(contains2)
# part 2: 801
