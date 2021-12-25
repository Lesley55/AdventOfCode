import math

input = "020D74FCE27E600A78020200DC298F1070401C8EF1F21A4D6394F9F48F4C1C00E3003500C74602F0080B1720298C400B7002540095003DC00F601B98806351003D004F66011148039450025C00B2007024717AFB5FBC11A7E73AF60F660094E5793A4E811C0123CECED79104ECED791380069D2522B96A53A81286B18263F75A300526246F60094A6651429ADB3B0068937BCF31A009ADB4C289C9C66526014CB33CB81CB3649B849911803B2EB1327F3CFC60094B01CBB4B80351E66E26B2DD0530070401C82D182080803D1C627C330004320C43789C40192D002F93566A9AFE5967372B378001F525DDDCF0C010A00D440010E84D10A2D0803D1761045C9EA9D9802FE00ACF1448844E9C30078723101912594FEE9C9A548D57A5B8B04012F6002092845284D3301A8951C8C008973D30046136001B705A79BD400B9ECCFD30E3004E62BD56B004E465D911C8CBB2258B06009D802C00087C628C71C4001088C113E27C6B10064C01E86F042181002131EE26C5D20043E34C798246009E80293F9E530052A4910A7E87240195CC7C6340129A967EF9352CFDF0802059210972C977094281007664E206CD57292201349AA4943554D91C9CCBADB80232C6927DE5E92D7A10463005A4657D4597002BC9AF51A24A54B7B33A73E2CE005CBFB3B4A30052801F69DB4B08F3B6961024AD4B43E6B319AA020020F15E4B46E40282CCDBF8CA56802600084C788CB088401A8911C20ECC436C2401CED0048325CC7A7F8CAA912AC72B7024007F24B1F789C0F9EC8810090D801AB8803D11E34C3B00043E27C6989B2C52A01348E24B53531291C4FF4884C9C2C10401B8C9D2D875A0072E6FB75E92AC205CA0154CE7398FB0053DAC3F43295519C9AE080250E657410600BC9EAD9CA56001BF3CEF07A5194C013E00542462332DA4295680"
input = "C200B40A82"

# "0" = 0000 but if an int is after the 0 like "02" = "00010" wich should be "00000010"
# works for most strings, but with the 0 it breaks because the first and last part produce a different bit for the starting 0
input = "".join(["0" for i in range(4 - len(str(bin(int(input[0], 16))[2:])))]) + str(bin(int(input, 16))[2:])

# quickfix for my specific input
# input = "000" + "".join(["0" for i in range(4 - len(str(bin(int(input[0], 16))[2:])))]) + str(bin(int(input, 16))[2:])
print(input)
def type_id(typeid, values):
    if typeid == 0:
        return sum(values)
    elif typeid == 1:
        return math.prod(values)
    elif typeid == 2:
        return min(values)
    elif typeid == 3:
        return max(values)
    elif typeid == 5:
        return 1 if values[0] > values[1] else 0
    elif typeid == 6:
        return 1 if values[0] < values[1] else 0
    elif typeid == 7:
        return 1 if values[0] == values[1] else 0

def package(i):
    print("i:"+str(i))
    id = input[i+3:i+6]
    i += 6
    typeid = int(id,2)
    value = None
    if typeid == 4:
        value = ""
        while True:
            value += input[i+1:i+5]
            if input[i] == "0":
                i += 5
                break
            i += 5
        value = int(value,2)
        print(value)
    else:
        ltid = input[i]
        lsub = ""
        if ltid == "0":
            lsub = int(input[i+1:i+16], 2) + i + 16
            i += 16
            values = []
            while i < lsub:
                p = package(i)
                i += p[0]
                values.append(p[1])
            value = type_id(typeid, values)
        else:
            lsub = int(input[i+1:i+12], 2)
            i += 12
            values = []
            for j in range(lsub):
                p = package(i)
                i += p[0]
                values.append(p[1])
            value = type_id(typeid, values)
    return [i, value]

print(package(0))

# part 2: 
