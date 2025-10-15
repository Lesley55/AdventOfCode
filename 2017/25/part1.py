steps = 12459852
states = {"A": [[True, 1, "B"], [True, -1, "E"]], "B": [[True, 1, "C"], [True, 1, "F"]], "C": [[True, -1, "D"], [False, 1, "B"]], "D": [[True, 1, "E"], [False, -1, "C"]], "E": [[True, -1, "A"], [False, 1, "D"]], "F": [[True, 1, "A"], [True, 1, "C"]]}
tape = {}
cursor = 0
state = "A"

for i in range(steps):
    s = states[state][1 if cursor in tape else 0]
    if s[0]:
        tape[cursor] = 1
    else:
        if cursor in tape:
            del tape[cursor]
    cursor += s[1]
    state = s[2]

print(len(tape))

# part 1: 4217
