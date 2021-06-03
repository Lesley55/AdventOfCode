replacements = ["Al => ThF", "Al => ThRnFAr", "B => BCa", "B => TiB", "B => TiRnFAr", "Ca => CaCa", "Ca => PB", "Ca => PRnFAr", "Ca => SiRnFYFAr", "Ca => SiRnMgAr", "Ca => SiTh", "F => CaF", "F => PMg", "F => SiAl", "H => CRnAlAr", "H => CRnFYFYFAr", "H => CRnFYMgAr", "H => CRnMgYFAr", "H => HCa", "H => NRnFYFAr", "H => NRnMgAr", "H => NTh", "H => OB", "H => ORnFAr", "Mg => BF", "Mg => TiMg", "N => CRnFAr", "N => HSi", "O => CRnFYFAr", "O => CRnMgAr", "O => HP", "O => NRnFAr", "O => OTi", "P => CaP", "P => PTi", "P => SiRnFAr", "Si => CaSi", "Th => ThCa", "Ti => BP", "Ti => TiTi", "e => HF", "e => NAl", "e => OMg"]
input = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

# replacements = ["e => H", "e => O", "H => HO", "H => OH", "O => HH"]
# input = "HOH"

short = 9999999999999999999999999999999

def f(e, n):
    global short
    if e == input:
        if n < short:
            short = n
            print(short)
        return
    if len(e) > len(input):
        return
    for i in replacements:
        r = i.split(" ")
        # trying to optimize a bit

        # if len(e) > 6:
        #     if e[0:len(e)-6] == input[0:len(e)-6]:
        #         for k in range(6):
        #             j = len(e)-5 + k
        #             if e[j:j+len(r[0])] == r[0]:
        #                 new = e[0:j] + r[2] + e[j+len(r[0]):len(e)]
        #                 f(new, n+1)
        
        for t in range(len(e)):
            if not e[t] == input[t]:
                for k in range(len(e)-t+1):
                    j = len(e)-t-1 + k
                    if e[j:j+len(r[0])] == r[0]:
                        new = e[0:j] + r[2] + e[j+len(r[0]):len(e)]
                        f(new, n+1)
                break
        
        # else:
        #     for j in range(len(e)):
        #         if e[j:j+len(r[0])] == r[0]:
        #             new = e[0:j] + r[2] + e[j+len(r[0]):len(e)]
        #             f(new, n+1)

f("e", 0)
print(short)

# part 2: bruteforcing all possible ways will take WAY to long