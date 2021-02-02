#Given At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the 
#GC-content of that string. Rosalind allows for a default error of 0.001 in all 
#decimal answers unless otherwise stated; please see the note on absolute error 
#below.

inputfile = '6_computing_GC_content_input.txt'

#empty dictionary for FASTA: sequence key-pairs
fasta_dict = {}

def GC_content(fasta_dict):

#placeholders to keep track of the current id of the max GC fasta string
    fasta_max = ''
    GC_max = 0

#calculates the gc percentage for each sequence and prints it
    for fasta_id, seq in fasta_dict.items():
        gc_percentage = (seq.count('G') + seq.count('C')) / len(seq) * 100
        message = f"The GC percentage of {fasta_id} is {round(gc_percentage, 6)}%"
        print(message)

#if the GC percentage calculated is higher than any previously calculated, save
#value over previous max
        if gc_percentage > GC_max:
            GC_max = gc_percentage
            fasta_max = fasta_id

    message = f"\nThe ID of the string with the highest GC is:\n\n{fasta_max}"
    "\n{round(GC_max, 6)}%"
    print(message)


#opens inputfile and stores lines as a list of strings
with open(inputfile) as file_object:
    lines = file_object.readlines()

#strips newline characters
for line in lines:
    line = line.strip()

#detects if the line contains the FASTA ID: if it does it creates a new key-pair
#in the dictionary. fasta_id temporarily stores the key for the next else statement
    if line[0] == '>':
        fasta_id = line.strip('>')
        fasta_dict[fasta_id] = ''

#Picks up the lines after the fasta_id, and assigns its value additively to the
#fasta_id key. += is necessary considering the sequence lines are spread across
#multiple lines rather than a single long line.
    else:
        fasta_dict[fasta_id] += line

GC_content(fasta_dict)