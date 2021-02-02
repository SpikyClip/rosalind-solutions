with open('2_transcribing_dna_into_rna_input.txt','r') as input_file:
    dna_sequence = input_file.read()

rna_sequence = dna_sequence.replace('T','U')

with open('2_transcribing_dna_into_rna_output.txt','w') as output_file:
    output_file.write(rna_sequence)

print(rna_sequence)