filename = 'IEV.txt'

with open(filename) as f:
    couples = [int(freq) for freq in f.read().split()]

# couples = [1, 0, 0, 1, 0, 1]

genodict = {}

genotypes = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']
pr_dom = [1, 1, 1, 0.75, 0.5, 0]

for genotype, probability, frequency in zip(genotypes, pr_dom, couples):
    offspring_no = frequency*2
    genodict[genotype] = probability * offspring_no

dominant_offspring_no = sum(genodict.values())

print(dominant_offspring_no)