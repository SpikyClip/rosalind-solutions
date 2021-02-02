with open('1_counting_dna_nucleotides.txt', 'r') as input_file:
    dna_sequence = str(input_file.readlines())

dna_dictionary = {
    'A': dna_sequence.count('A'),
    'C': dna_sequence.count('C'),
    'G': dna_sequence.count('G'),
    'T': dna_sequence.count('T'),
}

print(dna_dictionary.values())