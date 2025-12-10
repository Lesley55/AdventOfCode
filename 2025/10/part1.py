input = open("input.txt")

machines = []
for i in input:
   i = i.split("{")
   joltage = [int(j) for j in i[1][:-2].split(",")]
   i = i[0].split("]")
   lights = [j == "#" for j in i[0][1:]]
   i = i[1].strip().split(" ")
   buttons = [[int(j) for j in k[1:-1].split(",")] for k in i]
   machines.append([lights, buttons, joltage])

total = 0
for machine in machines:
   presses = 0
   buttons = machine[1]
   conf = [machine[0]]
   new = []
   while len(conf) > 0:
      l = conf.pop()
      for button in buttons:
         lights = l.copy()
         for i in button:
            lights[i] = not lights[i]
         if not lights in new:
            new.append(lights)
      if len(conf) == 0:
         presses += 1
         found = False
         for n in new:
            if not True in n:
               total += presses
               found = True
               break
         if found:
            break
         conf = new
         new = []

print(total)

# part 1: 425
