from itertools import permutations

input = open("input.txt")

packages = []
for i in input:
    packages.append(int(i))

third = sum(packages)/3 # 508

small = [9999999999999999,999999999999999]

for p in permutations(packages, len(packages)):
    for i in range(len(p[0:len(p)-2])):
        for j in range(len(p[i+1:len(p)-1])):
            for k in range(len(p[i+1+j+1:len(p)])):
                if sum(p[0:i+1]) == third and sum(p[i+1:i+1+j+1]) == third and sum(p[i+1+j+1:i+1+j+1+k+1]) == third:
                    if len(p[0:i+1]) < small[0]:
                        product = 1
                        for q in p[0:i+1]:
                            product *= q
                        small = [len(p[0:i+1]), product]
                    if len(p[i+1:i+1+j+1]) < small[0]:
                        product = 1
                        for q in p[i+1:i+1+j+1]:
                            product *= q
                        small = [len(p[i+1:i+1+j+1]), product]
                    if len(p[i+1+j+1:i+1+j+1+k+1]) < small[0]:
                        product = 1
                        for q in p[i+1+j+1:i+1+j+1+k+1]:
                            product *= q
                        small = [len(p[i+1+j+1:i+1+j+1+k+1]), product]

print(small)

# part 1: 