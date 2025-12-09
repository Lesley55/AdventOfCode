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

area = {}
for square in squares:
   for i in range(square[0], square[1] + 1):
      area[(i, square[2])] = True
      area[(i, square[3])] = True
   for i in range(square[2], square[3] + 1):
      area[(square[0], i)] = True
      area[(square[1], i)] = True

def inside(x, y, polygon):
   # assuming no holes because kind of eclipse
   left = False
   right = False
   for i in range(x + 1):
      if (y, x) in polygon:
         left = True
         break
   for i in range(x, 100000):
      if (y, x) in polygon:
         right = True
         break
   return left and right

for size in sizes:
   # corners
   a = tiles[size[1]]
   b = tiles[size[2]]
   c = [a[0], b[1]]
   d = [b[0], a[1]]
   if inside(a[0], a[1], area) and inside(b[0], b[1], area) and inside(c[0], c[1], area) and inside(d[0], d[1], area):
      print(size[0])
      break

# part 2: 4638024000 too high
# part 2: 4638024000 again
# part 2: 4518479420 too high
# part 2: 4638024000 again
# part 2: 4638024000 again
