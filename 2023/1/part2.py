input = open("input.txt")

total = 0
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i in input:
    d = ""
    for j in range(len(i)):
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
    for j in range(len(i))[::-1]:
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
    total += int(d)

print(total)

# part 2: 55686
