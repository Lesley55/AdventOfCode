input = open("input.txt")
input = input.readlines()

total = 0
grid = {}

for i in range(len(input)):
   for j in range(len(input[i])):
      if input[i][j] == "@":
         grid[(i, j)] = True

while True:
   removable = []
   for i in grid.keys():
      count = 0
      for j in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
         k = (i[0] + j[0], i[1] + j[1])
         if k in grid.keys():
            count += 1
      if count < 4:
         total += 1
         removable.append(i)
   if len(removable) == 0:
      break
   for i in removable:
      grid.pop(i)

print(total)

# part 2: 8623
