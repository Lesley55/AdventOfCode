input = open("input.txt")
rooms = []
realrooms = []

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
        realrooms.append(room)

for room in realrooms:
    id = room[len(room)-1].split("[")[0]

    text = ""
    for s in range(len(room)-1):
        text += room[s] + " "
 
    shift = int(id) % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    shifted = text.translate(table)

    if shifted == "northpole object storage ":
        print(id)

# part 2: 984
