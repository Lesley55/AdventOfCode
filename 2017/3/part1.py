input = 325489

spiral = 1
ring = 0
step = 8
while spiral < input:
    ring += 1
    spiral += ring * step
a = ring * step / 4
b = spiral - ring * step
c = input - b
d = c % a
e = a / 2
f = abs(d - e)
print(int(ring + f))

# part 1: 552
