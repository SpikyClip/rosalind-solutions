# url: http://rosalind.info/problems/hamm/

# Problem

# Given two strings s and t of equal length, the Hamming distance between
# s and t, denoted dH(s,t), is the number of corresponding symbols that
# differ in s and t. See Figure 2.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).


def hamdist(seq1, seq2):
    """Returns number of point mutations between two sequences"""
    point_mutations = (nuc1 != nuc2 for nuc1, nuc2 in zip(seq1, seq2))

    return sum(point_mutations)


if __name__ == "__main__":
    file1, file2 = "inputs/006_HAMM_input.txt", "outputs/006_HAMM_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        seq1, seq2 = f1.read().splitlines()
        f2.write(str(hamdist(seq1, seq2)))
