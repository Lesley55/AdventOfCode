input = open("input.txt")

paper = 0
ribbon = 0

for x in input:
    l, w, h = x.rstrip('\n').split('x')
    d = [int(l), int(w), int(h)]
    d.sort()
    paper += 2*d[0]*d[1] + 2*d[1]*d[2] + 2*d[0]*d[2] + d[0]*d[1]
    ribbon += 2*d[0] + 2*d[1] + d[0]*d[1]*d[2]

print(paper)
print(ribbon)