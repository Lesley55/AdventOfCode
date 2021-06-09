replacements = ["Al => ThF", "Al => ThRnFAr", "B => BCa", "B => TiB", "B => TiRnFAr", "Ca => CaCa", "Ca => PB", "Ca => PRnFAr", "Ca => SiRnFYFAr", "Ca => SiRnMgAr", "Ca => SiTh", "F => CaF", "F => PMg", "F => SiAl", "H => CRnAlAr", "H => CRnFYFYFAr", "H => CRnFYMgAr", "H => CRnMgYFAr", "H => HCa", "H => NRnFYFAr", "H => NRnMgAr", "H => NTh", "H => OB", "H => ORnFAr", "Mg => BF", "Mg => TiMg", "N => CRnFAr", "N => HSi", "O => CRnFYFAr", "O => CRnMgAr", "O => HP", "O => NRnFAr", "O => OTi", "P => CaP", "P => PTi", "P => SiRnFAr", "Si => CaSi", "Th => ThCa", "Ti => BP", "Ti => TiTi", "e => HF", "e => NAl", "e => OMg"]
input = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

# replacements = ["e => H", "e => O", "H => HO", "H => OH", "O => HH"]
# input = "HOH"

distinct = set()
distinct.add("e")

loops = 1
go = True
while go:
    dis = set()
    for b in distinct:
        for i in replacements:
            r = i.split(" ")
            for j in range(len(b)):
                if b[j:j+len(r[0])] == r[0]:
                    new = b[0:j] + r[2] + b[j+len(r[0]):len(b)]
                    if new == input:
                        print(loops)
                        go = False
                    elif not len(new) > len(input):
                        dis.add(new)
    distinct = dis

# part 2: bruteforcing all possible ways will take WAY to long