input = open("input.txt")
pw = "abcdefgh"

for i in input:
    i = i.strip().split()
    if i[0] == "swap":
        if i[1] == "position":
            swap = [int(i[2]), int(i[5])]
            mi = min(swap)
            ma = max(swap)
            pw = pw[:mi] + pw[ma] + pw[mi+1:ma] + pw[mi] + pw[ma+1:]
        elif i[1] == "letter":
            for j in range(len(pw)):
                if pw[j] == i[2]:
                    pw = pw[:j] + i[5] + pw[j+1:]
                elif pw[j] == i[5]:
                    pw = pw[:j] + i[2] + pw[j+1:]
    elif i[0] == "rotate":
        if i[1] == "left":
            pw = pw[1:] + pw[0]
        elif i[1] == "right":
            pw = pw[len(pw)-1] + pw[:len(pw)-1]
        elif i[1] == "based":
            index = pw.find(i[6])
            if index >= 4:
                index += 1
            index += 1
            for j in range(index):
                pw = pw[len(pw)-1] + pw[:len(pw)-1]
    elif i[0] == "reverse":
        x, y = int(i[2]), int(i[4])
        reverse = pw[x:y+1][::-1]
        pw = pw[:x] + reverse + pw[y+1:]
    elif i[0] == "move":
        x, y = int(i[2]), int(i[5])
        l = pw[x]
        pw = pw[:x] + pw[x+1:]
        pw = pw[:y] + l + pw[y:]

print(pw)

# part 1: fhagcedb(>= 4 ipv > 4) and becfhgad(??????) wrong

# alles appart getest, goede output, test voorbeeld erin gegooit, na elke stap goede antwoord, zou gwn moeten werken, idk wat er fout is
