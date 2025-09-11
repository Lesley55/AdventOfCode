input = open("input.txt")
input = input.readline()
input = input.split(",")

far = []
for i in range(len(input)):
    inp = input[:i+1]

    n = inp.count("n")
    ne = inp.count("ne")
    se = inp.count("se")
    s = inp.count("s")
    sw = inp.count("sw")
    nw = inp.count("nw")

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
    far.append(max(ns, ew))

print(max(far))

# part 2: 1424
