import re

input = open("input.txt")

def is_abba(substr):
    if substr[0] != substr[1] and substr[1] == substr[2] and substr[0] == substr[3]:
        return True
    return False

total = 0

for i in input:
    arr = re.split(r'\[|\]', i)
    tls_outside = False
    tls_inside = False
    for j in range(len(arr)):
        for k in range(len(arr[j])-3):
            substr = arr[j][k:k+4]
            abba = is_abba(substr)
            if j % 2 == 0 and abba:
                tls_outside = True
            elif abba:
                tls_inside = True
    if tls_inside:
        continue
    elif tls_outside:
        total += 1

print(total)

# part 1: 118
