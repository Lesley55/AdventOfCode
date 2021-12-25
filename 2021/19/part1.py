input = open("input.txt")

scanners = []

scanner = []
for i in input:
    if i[:3] == "---":
        scanner = []
    elif i == "\n":
        scanners.append(scanner)
    else:
        i = i.strip().split(",")
        scanner.append([int(j) for j in i])

def rotate_x(scanner):
    for i in scanner:
        pass

def rotate_y(scanner):
    for i in scanner:
        pass

def rotate_z(scanner):
    for i in scanner:
        pass

for s in scanners:
    for beacon in s:
        # rotations
        # check min/max to see difference and make them overlap
        # check if overlapping 12
        # add to list
        pass