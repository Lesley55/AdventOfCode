input = open("input.txt")

tiles = []
for i in input:
   i = i.strip().split(",")
   i = [int(i[0]), int(i[1])]
   tiles.append(i)

largest = 0
for i in range(len(tiles)):
   for j in range(i+1, len(tiles)):
      size = abs(tiles[i][0] - tiles[j][0] + 1) * abs(tiles[i][1] - tiles[j][1] + 1)
      if size > largest:
         largest = size

print(largest)

# part 1: 4748826374
