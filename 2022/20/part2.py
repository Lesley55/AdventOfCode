input = open("input.txt")

order = []
numbers = []
for i in input:
    i = i.strip()
    order.append(int(i) * 811589153)
    numbers.append(len(order) - 1)

for mix in range(10):
    for n in range(len(order)):
        i = numbers.index(n)
        numbers.pop(i)
        new = (i + order[n]) % len(numbers)
        numbers.insert(new, n)

sum = 0
for i in [1000, 2000, 3000]:
    sum += order[numbers[(numbers.index(order.index(0)) + i) % len(numbers)]]

print(sum)
# part 2: 10626948369382
