input = open("input.txt")
input = input.readlines()

operators = input[-1].strip().split()
problems = []
for i in range(len(input)-1):
   p = input[i].strip()
   p = p.split()
   p = [int(x) for x in p]
   problems.append(p)

total = 0
for i in range(len(operators)):
   add = True if operators[i] == "+" else False
   problem = 0 if add else 1
   for j in range(len(problems)):
      if add:
         problem += problems[j][i]
      else:
         problem *= problems[j][i]
   total += problem

print(total)

# part 1: 4648618073226
