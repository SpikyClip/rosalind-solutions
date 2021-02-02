from textwrap import wrap

def mRNA_trans(seq):
    '''translates a mRNA sequence to a protein sequence'''
    standard_genetic_code = {
        'F': ['UUU', 'UUC'], 
        'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'], 
        'I': ['AUU', 'AUC', 'AUA'], 
        'V': ['GUU', 'GUC', 'GUA', 'GUG'], 
        'M': ['AUG'], 
        'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 
        'P': ['CCU', 'CCC', 'CCA', 'CCG'], 
        'T': ['ACU', 'ACC', 'ACA', 'ACG'], 
        'A': ['GCU', 'GCC', 'GCA', 'GCG'], 
        'Y': ['UAU', 'UAC'], 
        'H': ['CAU', 'CAC'], 
        'N': ['AAU', 'AAC'], 
        'D': ['GAU', 'GAC'], 
        'STOP': ['UAA', 'UAG', 'UGA'], 
        'Q': ['CAA', 'CAG'], 
        'K': ['AAA', 'AAG'], 
        'E': ['GAA', 'GAG'], 
        'C': ['UGU', 'UGC'], 
        'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'], 
        'G': ['GGU', 'GGC', 'GGA', 'GGG'], 
        'W': ['UGG']}

    protein_seq = ''
#splits string into triplet codons in a list
    codons = wrap(seq, 3)
#Loops through codons, compares it to codon value in dictionary, and adds the 
#corresponding protein key to protein_seq string
    for codon in codons:
        for prot, value in standard_genetic_code.items():
            if codon in standard_genetic_code['STOP']:
                break
            elif codon in value:
                protein_seq += prot
    return protein_seq


filename = '7_PROT_translating_RNA_into_protein.txt'

with open(filename) as file_object:
    seq = file_object.read()

seq = seq[::3]

print(mRNA_trans(seq))