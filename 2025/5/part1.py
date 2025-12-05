input = open("input.txt")
input = input.readlines()

ranges = [x.strip().split("-") for x in input[:input.index("\n")]]
ingredients = [int(x.strip()) for x in input[input.index("\n") + 1:]]

total = 0
for i in ingredients:
   for j in ranges:
      range = int(j[0]), int(j[1])
      if range[0] <= i <= range[1]:
         total += 1
         break

print(total)

# part 1: 739
