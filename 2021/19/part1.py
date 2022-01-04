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
    rotated = []
    for i in scanner:
        rotated.append([i[2], i[1], i[0] * -1])
    return rotated

def rotate_y(scanner):
    rotated = []
    for i in scanner:
        rotated.append([i[1], i[0] * -1, i[2]])
    return rotated

beacons = scanners[0] # all beacons relative to the first scanner
scanners = scanners[1:]

# TODO #
def is_overlapping(s):
    # overlap relative position
    for i in None: #
        overlapping = 0
        for beacon in s:
            if abs(beacon) in abs(beacons): #
                overlapping += 1
        if overlapping >= 12:
            # add all beacons in current scanner with relative position to first scanner, to beacons/first scanner
            #
            return True
    return False

rs = None

def check_round():
    global rs
    # spin around for all orientations of that side
    for i in range(4):
        if is_overlapping(rs):
            return True
        rs = rotate_y(rs)
    return False

# maybe wrong ?
def check_scanner(s):
    global rs
    rs = s
    # turn to all sides of cube
    for i in range(3):
        if check_round(rs):
            return True
        rs = rotate_x
        if check_round(rs):
            return True
        rs = rotate_y
    return False

overlap = False
while True:
    if not overlap:
        break
    overlap = False
    for s in scanners:
        if check_scanner(s):
            overlap = True
            scanners.remove(s)

print(len(beacons))

# part 1: 
