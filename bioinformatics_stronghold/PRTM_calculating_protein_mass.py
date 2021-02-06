filename = "PRTM_monoisotopic_mass_table.txt"
with open(filename) as f:
    contents = f.read().split()

residues = contents[0::2]
masses = [float(mass) for mass in contents[1::2]]

mass_table = dict(zip(residues, masses))

def protein_mass(protein):
    total_mass = 0
    for residue in protein:
        total_mass += mass_table[residue]
    return total_mass

print(protein_mass("SKADYEK"))