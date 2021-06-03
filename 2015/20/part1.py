import math

input = 34000000

y = 1
while True:
    def divSum(num) :
        result = 0
        i = 2
        while i<= (math.sqrt(num)) :
            if (num % i == 0) :
                if (i == (num / i)) :
                    result = result + i
                else :
                    result = result + (i + num/i)
            i = i + 1
        return (result + 1)
    presents = divSum(y)

    if presents * 10 > input:
        print(y)
        break
    y += 1

# part 1: 831600 to high
#         1048320