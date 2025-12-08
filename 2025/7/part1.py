input = open("input.txt")
input = input.readlines()

splitters = []
for i in range(len(input)):
   for j in range(len(input[i])):
      if input[i][j] == "^":
         splitters.append([i,j])

beams = [[] for i in range(len(input))]
beams[0].append(input[0].index("S"))

total = 0
for i in range(1, len(input)):
   for b in beams[i-1]:
      if [i, b] in splitters:
         total += 1
         for j in [b-1, b+1]:
            if not j in beams[i]:
               beams[i].append(j)
      elif not b in beams[i]:
         beams[i].append(b)

print(total)

# part 1: 1690
