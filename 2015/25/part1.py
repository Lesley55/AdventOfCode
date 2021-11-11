a = 20151125
b = 252533
c = 33554393

row = 2947
column = 3029

r = 1
r2 = 1
col = 1
while True:
    if r2 == 1:
        r += 1
        r2 = r
        col = 1
    else:
        r2 -= 1
        col += 1
    a *= b
    a = a % c
    
    if r2 == row and col == column:
        print(a)
        break

# part 1: 19980801