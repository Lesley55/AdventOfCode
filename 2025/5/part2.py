input = open("input.txt")
input = input.readlines()

ranges = [x.strip().split("-") for x in input[:input.index("\n")]]

fresh = []
while len(ranges) > 0:
   i = ranges.pop(0)
   r = [int(i[0]), int(i[1])]
   for f in range(len(fresh)):
      if r[0] < fresh[f][0] and r[1] < fresh[f][0]:
         fresh.insert(f, r)
         break
      elif r[0] < fresh[f][0] and fresh[f][0] <= r[1] and r[1] <= fresh[f][1]:
         fresh[f][0] = r[0]
         ranges.insert(0, fresh.pop(f))
         break
      elif r[0] < fresh[f][0] and fresh[f][1] < r[1]:
         fresh[f][0] = r[0]
         fresh[f][1] = r[1]
         ranges.insert(0, fresh.pop(f))
         break
      elif fresh[f][0] <= r[0] and r[0] <= fresh[f][1] and r[1] <= fresh[f][1]:
         break
      elif fresh[f][0] <= r[0] and r[0] <= fresh[f][1] and fresh[f][1] < r[1]:
         fresh[f][1] = r[1]
         ranges.insert(0, fresh.pop(f))
         break
   else:
      fresh.append(r)

total = 0
for i in fresh:
   total += i[1] - i[0] + 1

print(total)

# part 2: 344486348901788
