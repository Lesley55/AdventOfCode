input = open("input.txt")
input = input.readlines()

regions = []
shapes = {}
s = 0
for i in input:
   if "x" in i:
      i = i.strip().split(": ")
      i = [int(x) for x in i[0].split("x") + i[1].split(" ")]
      regions.append(i)
   elif ":" in i:
      s = int(i[:i.index(":")])
      shapes[s] = []
   elif "#" in i:
      shapes[s].append(i.strip())

def rotate(shape):
   new = []
   for i in range(len(shape[0])):
      n = ""
      for j in range(len(shape)):
         n += shape[j][len(shape[j]) - i - 1]
      new.append(n)
   return new

def flip(shape):
   new = []
   for i in range(len(shape)):
      new.append(shape[i][::-1])
   return new

configurations = {}
for shape in shapes:
   configurations[shape] = [shapes[shape]]
   s = shapes[shape]
   for i in range(7):
      if i == 3:
         s = flip(s)
      else:
         s = rotate(s)
      if not s in configurations[shape]:
         configurations[shape].append(s)

def all_presents(pr):
   zero = True
   for p in pr:
      if p != 0:
         zero = False
         break
   return zero

def r(region, presents):
   for present in range(len(presents)):
      if presents[present] > 0:
         pr = presents.copy()
         pr[present] -= 1
         for shape in configurations[present]:
            for i in range(len(region) - len(shape) + 1):
               for j in range(len(region[i]) - len(shape[0]) + 1):
                  reg = region.copy()
                  for k in range(len(shape)):
                     for l in range(len(shape[k])):
                        if shape[k][l] == "#":
                           if reg[i + l][j + k] == ".":
                              reg[i + l] = reg[i + l][:j + k] + "#" + reg[i + l][j + k + 1:]
                              # reg[i + l] = reg[i + l][:j + k] + str(presents[present]) + reg[i + l][j + k + 1:]
                              # reg[i + l] = reg[i + l][:j + k] + str(present) + reg[i + l][j + k + 1:]
                           else:
                              reg = False
                              break
                     if reg == False:
                        break
                  if reg != False:
                     if all_presents(pr):
                        # for t in reg:
                        #    print(t)
                        # print("")
                        return True
                     else:
                        if r(reg, pr):
                           return True
         else:
            return False
   return False

total = 0
for i in regions:
   region = ["".join(["." for x in range(i[1])]) for y in range(i[0])]
   presents = i[2:]
   print(i)
   if r(region, presents):
      total += 1

print(total)

# part 1: 
