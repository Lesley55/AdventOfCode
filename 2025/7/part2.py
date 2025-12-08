input = open("input.txt")
input = input.readlines()

splitters = []
for i in range(len(input)):
   for j in range(len(input[i])):
      if input[i][j] == "^":
         splitters.append([i,j])

beams = [[0 for j in range(len(input[0]))] for i in range(len(input))]
beams[0][input[0].index("S")] = 1

for i in range(1, len(input)):
   for b in range(len(beams[i-1])):
      if beams[i-1][b] > 0:
         if [i, b] in splitters:
            for j in [b-1, b+1]:
               beams[i][j] += beams[i-1][b]
         else:
            beams[i][b] += beams[i-1][b]

print(sum(beams[-1]))

# part 2: 221371496188107
