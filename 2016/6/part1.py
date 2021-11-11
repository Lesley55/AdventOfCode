import string

input = open("input.txt")

alphabet = string.ascii_lowercase
all = {}

for i in input:
    for j in range(len(i)-1):
        index = alphabet.find(i[j])
        if index == -1:
            print(j)

        if not j in all:
            all[j] = {}
        
        if index in all[j]:
            all[j][index] += 1
        else:
            all[j][index] = 1

print(all)

message = ""
for i in all:
    most_occurring_char_index = max(all[i], key=all[i].get)
    message += alphabet[most_occurring_char_index]

print(message)

# part 1: asvcbhvg
