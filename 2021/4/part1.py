input = open("input.txt")
drawn = [46,12,57,37,14,78,31,71,87,52,64,97,10,35,54,36,27,84,80,94,99,22,0,11,30,44,86,59,66,7,90,21,51,53,92,8,76,41,39,77,42,88,29,24,60,17,68,13,79,67,50,82,25,61,20,16,6,3,81,19,85,9,28,56,75,96,2,26,1,62,33,63,32,73,18,48,43,65,98,5,91,69,47,4,38,23,49,34,55,83,93,45,72,95,40,15,58,74,70,89]

boards = [[]]
for i in input:
    i = i.strip().split()
    i = list(map(int, i))
    if i != []:
        boards[-1].append(i)
    else:
        boards.append([])

def mark(number):
    # mark drawn numbers as true
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for n in range(len(boards[board][row])):
                if boards[board][row][n] == number:
                    boards[board][row][n] = True

def winner():
    # check for winner
    for board in boards:
        for row in board:
            t = 0
            for n in row:
                if n == True:
                    t += 1
                else:
                    break
            if t == len(row):
                return board
        for column in range(len(board[0])):
            t = 0
            for row in range(len(board)):
                if board[row][column] == True:
                    t += 1
                else:
                    break
            if t == len(board[0]):
                return board
    return False

def score(board):
    sum = 0
    for row in board:
        for n in row:
            if n != True:
                sum += n
    return sum

for number in drawn:
    mark(number)
    board = winner()
    if board != False:
        print(score(board) * number)
        break

# part 1: 74320