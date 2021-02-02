filename = 'codon.txt'
with open(filename) as file_object:
    codonstr = file_object.read()

codonstr = codonstr.replace('\n', ' ')
codonlist = codonstr.split()

genetic_code = {}

for item in codonlist:
    if len(item) == 3:
        codon = item
    elif len(item) == 1 or item == 'Stop':
        prot = item.upper()
        if prot not in genetic_code:
            genetic_code[prot] = [codon]
        elif prot in genetic_code:
            genetic_code[prot] += [codon]

# for prot, codon in sorted(genetic_code.items()):
#     print(f"{prot}: {codon}")

print(genetic_code)