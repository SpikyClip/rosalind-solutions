# url: http://rosalind.info/problems/orf/

# Problem

# Either strand of a DNA double helix can serve as the coding strand for
# RNA transcription. Hence, a given DNA string implies six total reading
# frames, or ways in which the same region of DNA can be translated into
# amino acids: three reading frames result from reading the string
# itself, whereas three more result from reading its reverse complement.

# An open reading frame (ORF) is one which starts from the start codon
# and ends by stop codon, without any other stop codons in between.
# Thus, a candidate protein string is derived by translating an open
# reading frame into amino acids until a stop codon is reached.

# Given: A DNA string s of length at most 1 kbp in FASTA format.

# Return: Every distinct candidate protein string that can be translated
# from ORFs of s. Strings can be returned in any order.

import re

from common import fasta_to_dict, rev_complement, xna_to_prot


def open_frames(dna):
    """
    Returns a list containing tuples with information on the
    direction, offset, and sequence of valid open reading frames in dna
    sequence
    """
    start, stop, direction = "ATG", ["TAG", "TGA", "TAA"]
    strands, direction = (dna, rev_complement(dna)), ("forward", "reverse")
    orfs = list()

    # zipped directions with strands to retain direction information
    for direction, strand in zip(direction, strands):
        # rather than iterating through entire strand, find starting
        # positions of start codons first
        start_codons = [m.start() for m in re.finditer(r"ATG", strand)]
        # iterate through possible start positions
        for start_pos in start_codons:
            # steps one codon at a time until a stop codon is found
            for pos in range(start_pos + 3, len(strand), 3):
                codon = strand[pos : pos + 3]
                # if a stop codon is found, append orf
                if codon in stop:
                    # modulus is used to determine the offset of the orf
                    orf = (
                        direction,
                        start_pos % 3,
                        strand[start_pos : pos + 3],
                    )
                    orfs.append(orf)
                    break

    return orfs


if __name__ == "__main__":
    file1, file2 = "inputs/ORF_input.txt", "outputs/ORF_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        # creates fasta dict to deal with fasta format, but since there
        # is only one entry...
        dna = list(fasta_to_dict(f1.read()).values())[0]
        # unzips open_frame information, as only the orfs are pertinent
        _, _, orfs = zip(*open_frames(dna))
        # rosalind wants unique orfs, hence the use of set
        distinct_prot = set(map(xna_to_prot, orfs))
        for prot in distinct_prot:
            f2.write(prot + "\n")
