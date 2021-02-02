#Given: A file containing at most 1000 lines.
#Return: A file containing all the even-numbered lines from the original file. 
#Assume 1-based numbering of lines.

#Opens input file
with open('rosalind_ini5.txt', 'r') as input_file:
    contents = input_file.readlines()

even_lines = []

#returns index of each line, if index is not even, its 1 base number is even
#appends even line to empty list
for line in contents:
    if contents.index(line) % 2 != 0:
        even_lines.append(line)

#writes even lines to output file
with open('output.txt', 'w') as output_file:
    for line in even_lines:
        output_file.write(str(line))