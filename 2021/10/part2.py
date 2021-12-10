input = open("input.txt")

corrupted = []
open = "{[(<"
chunks = {
    "}": "{",
    "]": "[",
    ")": "(",
    ">": "<",
}
scores = []
for i in input:
    i = i.strip()
    current = []
    incomplete = True
    for j in i:
        if j in open:
            current.append(j)
        elif chunks[j] == current[-1]:
            current.pop(-1)
        else:
            corrupted.append(j)
            incomplete = False
            break
    if incomplete:
        current.reverse()
        score = 0
        for i in current:
            score *= 5
            if i == "(":
                score += 1
            elif i == "[":
                score += 2
            elif i == "{":
                score += 3
            elif i == "<":
                score += 4
        scores.append(score)

scores.sort()
print(scores[int((len(scores) - 1)/2)])

# part 2: 3646451424
