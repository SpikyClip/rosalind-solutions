# url: http://rosalind.info/problems/revc/

# Problem

# In DNA strings, symbols 'A' and 'T' are complements of each other, as
# are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by
# reversing the symbols of s, then taking the complement of each symbol
# (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.

from common import rev_complement


if __name__ == "__main__":
    file1, file2 = "inputs/REVC_input.txt", "outputs/REVC_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        dna_seq = f1.read().strip()
        f2.write(rev_complement(dna_seq))