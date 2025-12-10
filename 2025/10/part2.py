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
   joltages = machine[2]
   conf = [[0 for i in joltages]]
   new = []
   while len(conf) > 0:
      l = conf.pop()
      for button in buttons:
         joltage = l.copy()
         for i in button:
            joltage[i] += 1
         for i in range(len(joltages)):
            if joltage[i] > joltages[i]:
               break
         else:
            if not joltage in new:
               new.append(joltage)
      if len(conf) == 0:
         presses += 1
         found = False
         for n in new:
            d = False
            if n[0] > 0:
               d = True
               fraction = joltages[0] / n[0]
               for i in range(1, len(n)):
                  if n[i] == 0 or fraction != joltages[i] / n[i]:
                     d = False
                     break
            if n == joltages or (d and n[0] > 0 and joltages[0] % n[0] == 0):
               print(presses)
               total += presses
               found = True
               break
         if found:
            break
         conf = new
         new = []

print(total)

# part 2: 
