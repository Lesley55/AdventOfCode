input = open("input.txt")

devices = {}
for i in input:
    i = i.strip().split(": ")
    devices[i[0]] = i[1].split(" ")

paths = 0

def r(device, dac, fft):
   paths = 0
   for i in devices[device]:
      if i == "out":
         if dac and fft:
            paths += 1
      else:
         if i == "dac":
            dac = True
         if i == "fft":
            fft = True
         result = r(i, dac, fft)
         paths += result[0]
   return [paths, dac, fft]

print(r("svr", False, False)[0])

# part 2: 
