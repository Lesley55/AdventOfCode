input = open("input.txt")
input = input.readlines()

operators = input[-1].strip().split()
problems = []
for i in range(len(input)-1):
   p = input[i].replace("\n","")
   problems.append(p)

numbers = []
columns = []
for i in range(len(problems[0])):
   num = ""
   for j in range(len(problems)):
      num += problems[j][i]
   if num.strip().isdigit():
      numbers.append(int(num))
   else:
      columns.append(numbers)
      numbers = []
columns.append(numbers)

answers = 0
total = 0
for c in columns:
   add = True if operators[answers] == "+" else False
   problem = 0 if add else 1
   for n in range(len(c)):
      if add:
         problem += c[n]
      else:
         problem *= c[n]
   total += problem
   answers += 1

print(total)

# part 2: 7329921182115
