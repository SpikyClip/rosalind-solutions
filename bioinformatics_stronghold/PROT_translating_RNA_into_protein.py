# url: http://rosalind.info/problems/prot/

# Problem

# The 20 commonly occurring amino acids are abbreviated by using 20 letters
# from the English alphabet (all letters except for B, J, O, U, X, and Z).
# Protein strings are constructed from these 20 symbols. Henceforth, the
# term genetic string will incorporate protein strings along with DNA
# strings and RNA strings.

# The RNA codon table dictates the details regarding the encoding of
# specific codons into the amino acid alphabet.

# Given: An RNA string s corresponding to a strand of mRNA (of length at
# most 10 kbp).

# Return: The protein string encoded by s.


def get_codon_table(file):
    """Returns dict of protein: codons from codon.txt"""
    content = file.read().split()
    codon, prot = content[0::2], content[1::2]
    codon_table = dict()

    for codon, prot in zip(codon, prot):
        codon_table[codon] = prot
    return codon_table


def str_to_codons(seq):
    """Splits a string of codons into a list of codons"""
    codons = [seq[i : i + 3] for i in range(0, len(seq), 3)]
    return codons


def codon_to_prot(codons, codon_table):
    """Converts codons to proteins according to codon table, excluding Stop"""
    prot = "".join(
        [codon_table[codon] for codon in codons if codon_table[codon] != "Stop"]
    )
    return prot


if __name__ == "__main__":
    file1, file2, file3 = (
        "inputs/RNA_codon_table.txt",
        "inputs/PROT_input.txt",
        "outputs/PROT_output.txt",
    )

    with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "w") as f3:
        codon_table, codons = get_codon_table(f1), str_to_codons(
            f2.read().strip()
        )
        prot = codon_to_prot(codons, codon_table)
        f3.write(prot)