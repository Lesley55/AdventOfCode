input = open("input.txt")
input = input.readline()
input = input.split(",")
input = list(map(int, input))

hashlist = [i for i in range(256)]
current = 0
skip_size = 0

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

print(hashlist[0] * hashlist[1])

# part 1: 40132
