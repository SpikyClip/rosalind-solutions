# url: http://rosalind.info/problems/mrna/

# Problem

# For positive integers a and n, a modulo n (written amodn in shorthand)
# is the remainder when a is divided by n. For example, 29mod11=7
# because 29=11×2+7.

# Modular arithmetic is the study of addition, subtraction, multiplication,
# and division with respect to the modulo operation. We say that a and b
# are congruent modulo n if amodn=bmodn; in this case, we use the
# notation a≡bmodn.

# Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn,
# then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these
# rules, you may wish to verify these relationships for a=29, b=73, c=10,
# d=32, and n=11.

# As you will see in this exercise, some Rosalind problems will ask for
# a (very large) integer solution modulo a smaller number to avoid the
# computational pitfalls that arise with storing such large numbers.

# Given: A protein string of length at most 1000 aa.

# Return: The total number of different RNA strings from which the
# protein could have been translated, modulo 1,000,000. (Don't neglect
# the importance of the stop codon in protein translation.)

import numpy as np


def prot_to_mrna_no(protein):
    """
    Counts the number of each type of amino acid in protein, appending the
    number of permutations possible for each amino acid type to the power of
    the count to a list. The product of this list is returned as a modulo of
    1_000_000.
    """

    # dict containing the number of possible codons for each amino acid
    aa_permutations = {
        "F": 2,
        "L": 6,
        "I": 3,
        "V": 4,
        "M": 1,
        "S": 6,
        "P": 4,
        "T": 4,
        "A": 4,
        "Y": 2,
        "H": 2,
        "N": 2,
        "D": 2,
        "Q": 2,
        "K": 2,
        "E": 2,
        "C": 2,
        "R": 6,
        "G": 4,
        "W": 1,
    }

    # 3 ** 1 is the initial value in the list, as proteins must have 1
    # stop codon and there are only 3 permutations to a stop codon
    total_no = [3]

    # Loops through all amino acids and counts its frequency in
    # protein. The possible mRNA combinations for that amino acid are
    # appended as permutations to the power of its count, modulus
    # 1_000_000 which saves some computational power
    for amino_acid, permute in aa_permutations.items():
        aa_count = protein.count(amino_acid)
        total_no.append(pow(permute, aa_count, 1_000_000))

    result = np.prod(total_no) % 1_000_000

    return result


if __name__ == "__main__":
    file1, file2 = "inputs/MRNA_input.txt", "outputs/MRNA_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        protein = f1.read().strip()
        total_no = prot_to_mrna_no(protein)
        f2.write(str(total_no))
