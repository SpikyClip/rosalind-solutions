def reverse_complement(seq):
    '''Returns the reverse complement of a DNA nucleotide sequence'''
    complement_table = str.maketrans('ATCG','TAGC')
    complement_seq = seq[::-1].translate(complement_table)
    return complement_seq

seq = 'GTACGCTGGAAAAAGCCTGAAAGCTTACT'.upper()

print(reverse_complement(seq))

# rev = 'CTCCAGCTTGTGCCCCAGGATG'[::-1]

# print(rev)