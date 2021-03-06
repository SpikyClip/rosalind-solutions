# url: http://rosalind.info/problems/splc/

# After identifying the exons and introns of an RNA string, we only need
# to delete the introns and concatenate the exons to form a new string
# ready for translation.

# Given: A DNA string s (of length at most 1 kbp) and a collection of
# substrings of s acting as introns. All strings are given in
# FASTA format.

# Return: A protein string resulting from transcribing and translating
# the exons of s. (Note: Only one solution will exist for the dataset
# provided.)

import re
from common import fasta_to_dict, xna_to_prot


def splice(dna, introns):
    """
    Given a dna string and intron substrings as list, removes introns
    from dna in one pass returning spliced string
    """
    intron_pattern = re.compile("|".join(introns))
    # uses re.sub to remove introns in one pass
    splice = intron_pattern.sub(lambda m: "", dna)

    return splice


if __name__ == "__main__":
    file1, file2 = "inputs/SPLC_input.txt", "outputs/SPLC_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        dna, *introns = list(fasta_to_dict(f1.read()).values())
        splice = splice(dna, introns)
        prot = xna_to_prot(splice)
        f2.write(prot)