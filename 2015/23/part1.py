input = ["jio a, +16", "inc a", "inc a", "tpl a", "tpl a", "tpl a", "inc a", "inc a", "tpl a", "inc a", "inc a", "tpl a", "tpl a", "tpl a", "inc a", "jmp +23", "tpl a", "inc a", "inc a", "tpl a", "inc a", "inc a", "tpl a", "tpl a", "inc a", "inc a", "tpl a", "inc a", "tpl a", "inc a", "tpl a", "inc a", "inc a", "tpl a", "inc a", "tpl a", "tpl a", "inc a", "jio a, +8", "inc b", "jie a, +4", "tpl a", "inc a", "jmp +2", "hlf a", "jmp -7"]

register = {"a": 0, "b": 0}
register = {"a": 1, "b": 0}

i = 0
while True:
    if i >= len(input) or i < 0:
        break
    j = input[i].replace(",", "").split(" ")
    if j[0] == "hlf":
        register[j[1]] /= 2
    elif j[0] == "tpl":
        register[j[1]] *= 3
    elif j[0] == "inc":
        register[j[1]] += 1
    elif j[0] == "jmp":
        i += int(j[1])
        continue
    elif j[0] == "jie":
        if register[j[1]] % 2 == 0:
            i += int(j[2])
            continue
    elif j[0] == "jio":
        if register[j[1]] == 1:
            i += int(j[2])
            continue
    i += 1

print(register["b"])

# part 1: 170
# part 1: 247