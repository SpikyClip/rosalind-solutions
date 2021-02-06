# url: http://rosalind.info/problems/dna/

# Problem

# A string is simply an ordered collection of symbols selected from some
# alphabet and formed into a word; the length of a string is the number
# of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the
# symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective
# number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.


def nucleotide_count(dna_seq):
    """Returns string of nucleotide counts in order A C G T from dna_seq"""

    result = list()
    dna_dict = {
        "A": dna_seq.count("A"),
        "C": dna_seq.count("C"),
        "G": dna_seq.count("G"),
        "T": dna_seq.count("T"),
    }

    for count in dna_dict.values():
        result.append(str(count))
    result = " ".join(result)

    return result


if __name__ == "__main__":
    file1, file2 = "inputs/DNA_input.txt", "outputs/DNA_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        dna_seq = f1.read().strip()
        f2.write(nucleotide_count(dna_seq))