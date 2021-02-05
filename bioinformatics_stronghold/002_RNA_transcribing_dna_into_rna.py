# url: http://rosalind.info/problems/rna/

# Problem

# An RNA string is a string formed from the alphabet containing 'A', 'C',
# 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed
# RNA string u is formed by replacing all occurrences of 'T' in t with
# 'U' in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.


def dna_to_rna(dna_seq):
    """Transcribes a DNA string to RNA"""
    rna_seq = dna_seq.replace("T", "U")
    return rna_seq


if __name__ == "__main__":
    file1, file2 = "inputs/002_RNA_input.txt", "outputs/002_RNA_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        dna_seq = f1.read().strip()
        f2.write(dna_to_rna(dna_seq))