input = "hepxcrrq"

a = "abcdefghijklmnopqrstuvwxyza"

def incr(n):
    global input
    next = False
    z = False
    for l in a:
        if next:
            new = input[0:n] + l
            if n+1 < len(input):
                new += input[n+1:len(input)]
            input = new
            if z:
                if not n < 1:
                    incr(n-1)
            break
        elif input[n] == l:
            next = True
            if l == "z":
                z = True

def valid():
    three = False
    for i in range(len(a) - 3):
        if a[i:i+3] in input:
            three = True
    if not three:
        return False

    if "i" in input or "o" in input or "l" in input:
        return False
    
    pairs = 0
    for i in range(len(a) - 1):
        pair = a[i] + a[i]
        if pair in input:
            pairs += 1
    if pairs < 2:
        return False

    return True

while True:
    incr(len(input)-1)
    if valid():
        print(input)
        break

# part 1: hepxxyzz