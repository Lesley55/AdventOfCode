from ast import literal_eval
import math

input = open("input.txt")

class Pair:
    def __init__(self, arr):
        if isinstance(arr[0], list):
            self.left = Pair(arr[0])
        else:
            self.left = arr[0]
        if isinstance(arr[1], list):
            self.right = Pair(arr[1])
        else:
            self.right = arr[1]
    
    def addright(self, value):
        if isinstance(self.left, Pair):
            self.left.addright(value)
        else:
            self.left += value
    
    def addleft(self, value):
        if isinstance(self.right, Pair):
            self.right.addleft(value)
        else:
            self.right += value

    def explode(self, deep):
        if isinstance(self.left, Pair):
            if deep >= 4:
                if not isinstance(self.right, Pair):
                    self.right += self.left.right
                    return [self.left.left, 0]
                addtoside = [self.left.left, self.left.right]
                self.left = 0
                return addtoside
            else:
                res = self.left.explode(deep + 1)
                if res != False:
                    if isinstance(self.right, Pair):
                        self.right.addright(res[1])
                        return [res[0], 0]
                    else:
                        self.right += res[1]
                        return [res[0], 0]
                return False
        if isinstance(self.right, Pair):
            if deep >= 4:
                if not isinstance(self.left, Pair):
                    self.left += self.right.left
                    return [0, self.right.right]
                addtoside = [self.right.left, self.right.right]
                self.right = 0
                return addtoside
            else:
                res = self.right.explode(deep + 1)
                if res != False:
                    if isinstance(self.left, Pair):
                        self.left.addleft(res[0])
                        return [0, res[1]]
                    else:
                        self.left += res[0]
                        return [0, res[1]]
                return False
        return False

    def split(self):
        if not isinstance(self.left, Pair):
            if self.left >= 10:
                self.left = Pair([math.floor(self.left / 2), math.ceil(self.left / 2)])
                return True
        else:
            if self.left.split():
                return True
        if not isinstance(self.right, Pair):
            if self.right >= 10:
                self.right = Pair([math.floor(self.right / 2), math.ceil(self.right / 2)])
                return True
        else:
            return self.right.split()
        return False

    def magnitude(self):
        mag = 0
        if isinstance(self.left, Pair):
            mag += 3 * self.left.magnitude()
        else:
            mag += 3 * self.left
        if isinstance(self.right, Pair):
            mag += 2 * self.right.magnitude()
        else:
            mag += 2 * self.right
        return mag

pair = None

def reduce():
    while True:
        explode = False
        split = False
        while True:
            if pair.explode(0) != False:
                break
            else:
                explode = True
        while True:
            if not pair.split():
                break
            else:
                split = True
                break
        if not explode and not split:
            break

for i in input:
    i = i.strip()
    i = literal_eval(i)
    if not pair:
        pair = Pair(i)
    else:
        pair = Pair([pair, i])
    # reduce()

print(pair.magnitude())

# part 1: 
