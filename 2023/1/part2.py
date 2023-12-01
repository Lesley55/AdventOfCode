input = open("input.txt")

total = 0
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d = ""

def get_number(i, a):
    global d
    for j in a:
        if i[j].isdigit():
            d += i[j]
            break
        found = False
        for w in words:
            if i[j:j+len(w)] == w:
                d += str(words.index(w) + 1)
                found = True
                break
        if found:
            break

for i in input:
    get_number(i, range(len(i)))
    get_number(i, range(len(i))[::-1])
    total += int(d)
    d = ""

print(total)

# part 2: 55686
