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

message_part_1 = ""
message_part_2 = ""
for i in all:
    most_occurring_char_index = max(all[i], key=all[i].get)
    least_occurring_char_index = min(all[i], key=all[i].get)
    message_part_1 += alphabet[most_occurring_char_index]
    message_part_2 += alphabet[least_occurring_char_index]

print(message_part_1)
print(message_part_2)

# part 1: asvcbhvg
# part 2: odqnikqv
