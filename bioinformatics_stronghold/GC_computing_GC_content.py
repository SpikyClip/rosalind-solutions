# url: http://rosalind.info/problems/gc/

# Problem

# The GC-content of a DNA string is given by the percentage of symbols in
# the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG"
# is 37.5%. Note that the reverse complement of any DNA string has the same
# GC-content.

# DNA strings must be labeled when they are consolidated into a database.
# A commonly used method of string labeling is called FASTA format. In
# this format, the string is introduced by a line that begins with '>',
# followed by some labeling information. Subsequent lines contain the
# string itself; the first line to begin with '>' indicates the label of
# the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled
# by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between
# 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp
# each).

# Return: The ID of the string having the highest GC-content, followed by
# the GC-content of that string. Rosalind allows for a default error of
# 0.001 in all decimal answers unless otherwise stated; please see the note
# on absolute error below.


def fasta_to_dict(file):
    """Parses file object and returns dictionary of ID keys and seq values"""
    seq_dict = dict()
    # opens file as list of lines without \n chars
    line_list = file.read().splitlines()

    # parses line_list, storing names and seq in seq_dict
    for line in line_list:
        if line.startswith(">"):
            seq_name = line.lstrip(">")
            seq_dict[seq_name] = ""
        else:
            seq_dict[seq_name] += line.upper()

    return seq_dict


def GC_percent(seq):
    """Returns GC content as a percentage to 3 decimal places"""
    gc_count = seq.count("G") + seq.count("C")
    gc_percent = (gc_count / len(seq)) * 100

    return round(gc_percent, 3)


def max_GC(seq_dict):
    max_id = max(seq_dict, key=lambda id: GC_percent(seq_dict[id]))
    return max_id, GC_percent(seq_dict[max_id])


if __name__ == "__main__":
    file1, file2 = "inputs/GC_input.txt", "outputs/GC_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        seq_dict = fasta_to_dict(f1)
        id, gc_percent = max_GC(seq_dict)
        f2.write(f"{id}\n{gc_percent}")