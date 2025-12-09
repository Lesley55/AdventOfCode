input = open("input.txt")

tiles = []
for i in input:
   i = i.strip().split(",")
   i = [int(i[0]), int(i[1])]
   tiles.append(i)

sizes = []
ylines = []
xlines = []
for i in range(len(tiles)):
   for j in range(i+1, len(tiles)):
      size = abs(tiles[i][0] - tiles[j][0] + 1) * abs(tiles[i][1] - tiles[j][1] + 1)
      sizes.append([size, i, j])
      if tiles[i][0] == tiles[j][0]:
         y = [tiles[i], tiles[j]]
         y.sort(key=lambda i: i[1])
         ylines.append(y)
      elif tiles[i][1] == tiles[j][1]:
         x = [tiles[i], tiles[j]]
         x.sort(key=lambda i: i[0])
         xlines.append(x)

sizes.sort(key=lambda x: x[0], reverse=True)
ylines.sort(key=lambda i: i[0][0])
xlines.sort(key=lambda i: i[0][1])

squares = []
for i in range(len(ylines)):
   for j in range(i+1, len(ylines)):
      a = max([ylines[i][0][1], ylines[j][0][1]])
      b = min([ylines[i][1][1], ylines[j][1][1]])
      if a <= b:
         squares.append([a, b, ylines[i][0][0], ylines[j][0][0]])
for i in range(len(xlines)):
   for j in range(i+1, len(xlines)):
      a = max([xlines[i][0][0], xlines[j][0][0]])
      b = min([xlines[i][1][0], xlines[j][1][0]])
      if a <= b:
         squares.append([xlines[i][0][1], xlines[j][0][1], a, b])

# visual representation
for i in range(0, 100000, 2000):
   row = ""
   for j in range(0, 100000, 2000):
      for square in squares:
         if j >= square[0] and j <= square[1] and i >= square[2] and i <= square[3]:
            row += "#"
            break
      else:
         row += "."
   print(row)

# seems to be eclipse, dont know the exact size, but maybe use math to get biggest rectangle in eclipse to get closer to the answer
o = [x[0] for x in tiles]
p = [x[1] for x in tiles]
e1 = max(o) - min(o)
e2 = max(p) - min(p)
print(int(2* (e1/2) * (e2/2))) # 4652758465
# possible size should probably be smaller than this max area

for size in sizes:
   print(size)
   inside = True
   a = [tiles[size[1]][0], tiles[size[2]][0]]
   for i in range(min(a), max(a) + 1):
      b = [tiles[size[1]][1], tiles[size[2]][1]]
      j = min(b)
      # for j in range(min(b), max(b) + 1):
      while j <= max(b):
         for square in squares:
            if j >= square[0] and j <= square[1] and i >= square[2] and i <= square[3]:
               j = square[1]
               break
         else:
            inside = False
            break
         j += 1
      if not inside:
         break
   if inside:
      print(size[0])
      break

# part 2: 4638024000 too high
