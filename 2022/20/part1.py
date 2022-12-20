input = open("input.txt")

order = []
numbers = []
for i in input:
    i = i.strip()
    order.append(int(i))
    numbers.append(int(i))

for n in order:
    i = numbers.index(n)
    numbers.pop(i)
    new = (i + n) % len(numbers)
    ## for checking to make it visually the same as example when printing, but doesn't change the order
    # if new == 0:
    #     numbers.append(n)
    # else:
    numbers.insert(new, n)
    # print(n, numbers)

sum = 0
for i in [1000, 2000, 3000]:
    sum += numbers[(numbers.index(0) + i) % len(numbers)]
    # print(numbers[(numbers.index(0) + i) % len(numbers)])

print(sum)
# part 1: -3850 wrong
