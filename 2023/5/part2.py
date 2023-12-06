input = open("input.txt")
input = input.readlines()

seeds = [int(i) for i in input[0].split()[1:]]
new_seeds = []
unused = []

def use(n, r):
    for u in range(0, len(unused), 2):
        if n <= unused[u] and unused[u] <= n + r:
            if n + r < unused[u] + unused[u+1]:
                unused[u+1] = unused[u] + unused[u+1] - n - r
                unused[u] = n + r
            else:
                unused.pop(u)
                unused.pop(u)
                use(n, r)
                break
        elif unused[u] < n and n <= unused[u] + unused[u+1]:
            if unused[u] + unused[u+1] <= n + r:
                unused[u+1] = n - unused[u]
            else:
                unused.append(n + r)
                unused.append(unused[u] + unused[u+1] - n - r)
                unused[u+1] = n - unused[u]

def insert(n, r):
    inserted = False
    for i in range(0, len(new_seeds), 2):
        if n < new_seeds[i]:
            if new_seeds[i] < n + r:
                if n + r < new_seeds[i] + new_seeds[i+1]:
                    new_seeds[i+1] = new_seeds[i] + new_seeds[i+1] - n
                else:
                    new_seeds[i+1] = r
                new_seeds[i] = n
            else:
                new_seeds.insert(i, n)
                new_seeds.insert(i+1, r)
            inserted = True
            break
        elif n <= new_seeds[i] + new_seeds[i+1]:
            if new_seeds[i] + new_seeds[i+1] < n + r:
                if i+2 < len(new_seeds) and new_seeds[i+2] < n + r:
                    new_seeds[i+1] = new_seeds[i+2] + new_seeds[i+3] - new_seeds[i]
                    new_seeds.pop(i+2)
                    new_seeds.pop(i+2)
                    if new_seeds[i] + new_seeds[i+1] < n + r:
                        insert(n, r)
                else:
                    new_seeds[i+1] = n + r - new_seeds[i]
            inserted = True
            break
    if not inserted:
        new_seeds.append(n)
        new_seeds.append(r)

def check(k, s):
    if k[1] <= seeds[s] and seeds[s] < k[1] + k[2]:
        if seeds[s] + seeds[s+1] <= k[1] + k[2]:
            insert(k[0] + seeds[s] - k[1], seeds[s+1])
            use(seeds[s], seeds[s+1])
        else:
            insert(k[0] + seeds[s] - k[1], k[1] + k[2] - seeds[s])
            use(seeds[s], k[2])
    elif seeds[s] < k[1] and k[1] < seeds[s] + seeds[s+1]:
        if seeds[s] + seeds[s+1] < k[1] + k[2]:
            insert(k[0], seeds[s] + seeds[s+1] - k[1])
            use(k[1], seeds[s] + seeds[s+1] - k[1])
        else:
            insert(k[0], k[2])
            use(k[1], k[2])

for i in range(len(input)):
    if "map:" in input[i]:
        unused = [s for s in seeds]
        for j in input[i+1:]:
            if j == "\n":
                break
            k = [int(l) for l in j.split()]
            for s in range(0, len(seeds), 2):
                check(k, s)
        for u in range(0, len(unused), 2):
            for i in range(0, len(new_seeds), 2):
                if unused[u] < new_seeds[i]:
                    new_seeds.insert(i, unused[u])
                    new_seeds.insert(i+1, unused[u+1])
                    break
            else:
                new_seeds.append(unused[u])
                new_seeds.append(unused[u+1])
        seeds = new_seeds
        new_seeds = []

print(min(seeds[::2]))

# part 2: 136096660
