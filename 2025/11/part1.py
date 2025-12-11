input = open("input.txt")

devices = {}
for i in input:
    i = i.strip().split(": ")
    devices[i[0]] = i[1].split(" ")

paths = 0

def r(d):
   paths = 0
   for i in devices[d]:
      if i == "out":
         paths += 1
      else:
         paths += r(i)
   return paths

print(r("you"))
        
# part 1: 613
