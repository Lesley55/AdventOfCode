from itertools import permutations

input = ["Faerun to Norrath = 129", "Faerun to Tristram = 58", "Faerun to AlphaCentauri = 13", "Faerun to Arbre = 24", "Faerun to Snowdin = 60", "Faerun to Tambi = 71", "Faerun to Straylight = 67", "Norrath to Tristram = 142", "Norrath to AlphaCentauri = 15", "Norrath to Arbre = 135", "Norrath to Snowdin = 75", "Norrath to Tambi = 82", "Norrath to Straylight = 54", "Tristram to AlphaCentauri = 118", "Tristram to Arbre = 122", "Tristram to Snowdin = 103", "Tristram to Tambi = 49", "Tristram to Straylight = 97", "AlphaCentauri to Arbre = 116", "AlphaCentauri to Snowdin = 12", "AlphaCentauri to Tambi = 18", "AlphaCentauri to Straylight = 91", "Arbre to Snowdin = 129", "Arbre to Tambi = 53", "Arbre to Straylight = 40", "Snowdin to Tambi = 15", "Snowdin to Straylight = 99", "Tambi to Straylight = 70"]

city = set()

# get all cities
for i in input:
    c = i.split(" ")
    city.add(c[0])
    city.add(c[2])

small = 99999999999999

# loop all possible routes
for comb in permutations(city):
    dist = 0
    all = True
    for j in range(len(comb)):
        if j + 1 < len(comb):
            for n in input:
                c = n.split(" ")
                if (comb[j] == c[0] and comb[j+1] == c[2]) or (comb[j] == c[2] and comb[j+1] == c[0]):
                    dist += int(c[4])
                    break
            else:
                all = False  # only executed if the inner loop did NOT break
    
    if all:
        if dist < small:
            print(comb)
            small = dist

print(small)

# part 1: 719 high