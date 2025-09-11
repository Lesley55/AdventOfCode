input = open("input.txt")
input = input.readline()
# input = ''
# input = 'AoC 2017'
# input = '1,2,3'
# input = '1,2,4'

a = []
for i in input:
    a.append(ord(i))
input = a + [17, 31, 73, 47, 23]

hashlist = [i for i in range(256)]
current = 0
skip_size = 0

for round in range(64):
    for i in range(len(input)):
        end = current + input[i]
        wrap_around = 0
        if end > len(hashlist) - 1:
            wrap_around  = end - len(hashlist)
        sub = hashlist[current:end] + hashlist[0:wrap_around]
        reverse = sub[::-1]
        hashlist = reverse[len(reverse) - wrap_around:] + hashlist[wrap_around:current] + reverse[:len(reverse)-wrap_around] + hashlist[end:]
        current += input[i] + skip_size
        current %= len(hashlist)
        skip_size += 1

l = []
while len(hashlist) > 1:
    b = hashlist[0]
    for i in range(1, 16):
        b = b ^ hashlist[i]
    l.append(b)
    hashlist = hashlist[16:]

hash = ""
for i in l:
    hash += hex(i)[2:]

print(hash)

# part 2: 35b028fe2c958793f7d5a61d7a08c8 wrong

# all the examples give the correct answer, not sure why it doesn't work for my input
