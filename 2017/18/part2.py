import threading

input = open("input.txt")
input = input.readlines()

instructions = []
registers = {}
for i in input:
    r = i.strip().split(" ")
    if not r[1] in registers and r[1].isalpha():
        registers[r[1]] = 0
    instructions.append(r)

def getValue(a, r):
    if not a.isalpha():
        return int(a)
    else:
        return r[a]

def program(id):
    inst = instructions.copy()
    reg = registers.copy()
    reg["p"] = id
    q = queue0 if id == 0 else queue1
    otherq = queue1 if id == 0 else queue0
    jump = 0
    total = 0
    while True:
        if jump < 0 or jump >= len(inst):
            if total > 0:
                print(total)
            return
        if inst[jump][0] == "snd":
            if id == 1:
                total += 1
            otherq.append(getValue(inst[jump][1], reg))
        elif inst[jump][0] == "set":
            reg[inst[jump][1]] = getValue(inst[jump][2], reg)
        elif inst[jump][0] == "add":
            reg[inst[jump][1]] += getValue(inst[jump][2], reg)
        elif inst[jump][0] == "mul":
            reg[inst[jump][1]] *= getValue(inst[jump][2], reg)
        elif inst[jump][0] == "mod":
            reg[inst[jump][1]] %= getValue(inst[jump][2], reg)
        elif inst[jump][0] == "rcv":
            while True:
                if len(q) == 0:
                    if len(otherq) == 0:
                        if total > 0:
                            print(total)
                        return
                    continue
                reg[inst[jump][1]] = q.pop(0)
                break
        elif inst[jump][0] == "jgz":
            if getValue(inst[jump][1], reg) > 0:
                jump += getValue(inst[jump][2], reg)
                continue
        jump += 1

queue0 = []
queue1 = []

p0 = threading.Thread(target=program, args=(0,)).start()
p1 = threading.Thread(target=program, args=(1,)).start()

# part 2: 6858
