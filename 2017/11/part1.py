input = open("input.txt")
input = input.readline()
input = input.split(",")

n = input.count("n")
ne = input.count("ne")
se = input.count("se")
s = input.count("s")
sw = input.count("sw")
nw = input.count("nw")

n += ne
e = ne + se
s += sw
w = sw + nw

if n <= s:
    s -= n
    n -= n
else:
    n -= s
    s -= s

if e <= w:
    w -= e
    e -= e
else:
    e -= w
    w -= w

ns = abs(n-s)
ew = abs(e-w)
ans = max(ns, ew)

print(ans)

# part 1: 675
