from Bio import SeqIO

def GC_content(sequence):
    """Returns GC percentage of a string"""
    gc_percentage = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    return gc_percentage

dna_dict = {}

for sequence in SeqIO.parse('6_computing_GC_content_input.txt', "fasta"):
    dna_dict[sequence.id] = GC_content(sequence.seq)

print(max(dna_dict, key=dna_dict.get))
print(max(dna_dict.values()))