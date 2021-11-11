replacements = ["Al => ThF", "Al => ThRnFAr", "B => BCa", "B => TiB", "B => TiRnFAr", "Ca => CaCa", "Ca => PB", "Ca => PRnFAr", "Ca => SiRnFYFAr", "Ca => SiRnMgAr", "Ca => SiTh", "F => CaF", "F => PMg", "F => SiAl", "H => CRnAlAr", "H => CRnFYFYFAr", "H => CRnFYMgAr", "H => CRnMgYFAr", "H => HCa", "H => NRnFYFAr", "H => NRnMgAr", "H => NTh", "H => OB", "H => ORnFAr", "Mg => BF", "Mg => TiMg", "N => CRnFAr", "N => HSi", "O => CRnFYFAr", "O => CRnMgAr", "O => HP", "O => NRnFAr", "O => OTi", "P => CaP", "P => PTi", "P => SiRnFAr", "Si => CaSi", "Th => ThCa", "Ti => BP", "Ti => TiTi", "e => HF", "e => NAl", "e => OMg"]
input = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

distinct = set()

for i in replacements:
    r = i.split(" ")
    for j in range(len(input)):
        if input[j:j+len(r[0])] == r[0]:
            new = input[0:j] + r[2] + input[j+len(r[0]):len(input)]
            distinct.add(new)

print(len(distinct))

# part 1: 576