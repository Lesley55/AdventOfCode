input = open("input.txt")
pw = "fbgdceah"

# cant reverse through _io.TextIOWrapper so putting it in array first
arr = []
for i in input:
    arr.append(i)

for i in arr[::-1]:
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
        if i[1] == "right":
            for j in range(int(i[2])):
                pw = pw[1:] + pw[0]
        elif i[1] == "left":
            for j in range(int(i[2])):
                pw = pw[len(pw)-1] + pw[:len(pw)-1]
        elif i[1] == "based":
            for k in range(len(pw)):
                new = pw
                for j in range(k):
                    new = new[1:] + new[0]
                index = new.find(i[6])
                old = new
                if index >= 4:
                    index += 1
                index += 1
                for j in range(index):
                    new = new[len(new)-1] + new[:len(new)-1]
                if new == pw:
                    pw = old
                    break
    elif i[0] == "reverse":
        x, y = int(i[2]), int(i[4])
        reverse = pw[x:y+1][::-1]
        pw = pw[:x] + reverse + pw[y+1:]
    elif i[0] == "move":
        x, y = int(i[5]), int(i[2])
        l = pw[x]
        pw = pw[:x] + pw[x+1:]
        pw = pw[:y] + l + pw[y:]

print(pw)

# part 2: gdfcabeh
