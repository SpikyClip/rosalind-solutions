with open('3_complementing_a_strand_of_dna_input.txt','r') as input_file:
    primary_dna_sequence = input_file.read()
print(primary_dna_sequence)
complementary_dna_sequence = ''

for nucleotide in primary_dna_sequence:
    if nucleotide == 'A':
        complementary_dna_sequence += 'T'
    elif nucleotide == 'T':
        complementary_dna_sequence += 'A'
    elif nucleotide == 'C':
        complementary_dna_sequence += 'G'
    elif nucleotide == 'G':
        complementary_dna_sequence += 'C'

complementary_dna_sequence = complementary_dna_sequence[::-1]

with open('3_complementing_a_strand_of_dna_output.txt', 'w') as output_file:
    output_file.write(complementary_dna_sequence)

#Alternatively

translation_table = str.maketrans('ATCG','TAGC')
complementary_dna_sequence_1 = primary_dna_sequence[::-1].translate(translation_table)

print(complementary_dna_sequence_1)