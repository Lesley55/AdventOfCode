input = open("input.txt")

replacements = []
for i in input:
    i = i.strip()
    i = i.split(" => ")
    replacements.append(i)
input = replacements[-1][0]
replacements = replacements[:-2]

# hacky sort on length of second item, then on length first item assuming first item isnt longer then 9
def customsort(n):
    return int(str(len(n[1])) + str(len(n[0])))
replacements.sort(key=customsort, reverse=True)

# going backwards: reducing input by as much length as possible each step, to get to one letter asap
distinct = set()
distinct.add(input)
steps = 0
w = True
while w:
    steps += 1
    dis = set()
    for d in distinct:
        longestfoundreplacement = 0
        for i in replacements:
            if len(i) < longestfoundreplacement:
                break
            longestfoundreplacement = len(i)
            for j in range(len(d)):
                if d[j:j+len(i[1])] == i[1]:
                    new = d[:j] + i[0] + d[j+len(i[1]):]
                    if new == "e":
                        w = False
                    dis.add(new)
                    # break
    distinct = dis

print(steps)
# should skip a lot compaired to prev code, based on questionable assumptions, but will probably still take way to long
