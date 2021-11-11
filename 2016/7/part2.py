import re

input = open("input.txt")

def is_aba(substr):
    if substr[0] != substr[1] and substr[0] == substr[2]:
        return True
    return False

total = 0

for i in input:
    arr = re.split(r'\[|\]', i)
    outside = []
    inside = []
    for j in range(len(arr)):
        for k in range(len(arr[j])-2):
            substr = arr[j][k:k+3]
            aba = is_aba(substr)
            if j % 2 == 0 and aba:
                outside.append(substr[0:2])
            elif aba:
                inside.append(substr[1:3])
    ssl = False
    for i in outside:
        if i in inside:
            ssl = True
    if ssl:
        total += 1

print(total)

# part 2: 260 
