import json

input = open("input.txt")
input = input.read()
input = json.loads(input)

total = 0
def solve(i):
    global total
    if type(i) == list:
        for j in i:
            solve(j)
    elif type(i) == dict:
        for j in i.items():
            if "red" in j:
                return
        for j in i.items():
            for k in j:
                solve(k)
    elif type(i) == int:
        total += i

solve(input)
print(total)

# part 2: 96852