input = open("input.txt")
rooms = []

sum = 0

for i in input:
    rooms.append(i.split('-'))

for room in rooms:
    letters = []
    for r in range(len(room)-1):
        letters += list(room[r])

    letters = sorted(letters)

    occurrance = {}
    for l in letters:
        if l in occurrance:
            occurrance[l] += 1
        else:
            occurrance[l] = 1

    sortedocc = sorted(occurrance.items(), key=lambda item: item[1], reverse=True)
    
    five = ""
    for f in range(5):
        five += str(sortedocc[f][0])
    
    id, checksum = room[len(room)-1].split("[")
    if five == checksum[0:5]:
        sum += int(id)

print(sum)

# part 1: 185371
