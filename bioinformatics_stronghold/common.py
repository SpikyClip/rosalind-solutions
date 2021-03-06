import exceptions as ex


def rev_complement(dna_seq):
    """Returns the reverse complement of dna_seq as a string"""
    transl_tbl = str.maketrans("ATCG", "TAGC")
    rev_compl_seq = dna_seq[::-1].translate(transl_tbl)
    return rev_compl_seq


def fasta_to_dict(str):
    """Parses string and returns dictionary of ID keys and seq values"""
    seq_dict = dict()
    # splits string into lines without \n
    line_list = str.splitlines()

    # parses line_list, storing names and seq in seq_dict
    for line in line_list:
        if line.startswith(">"):
            seq_name = line.lstrip(">")
            seq_dict[seq_name] = ""
        else:
            seq_dict[seq_name] += line.upper()

    return seq_dict


def get_codon_table(file):
    """Returns dict of protein: codons from codon.txt"""
    content = file.read().split()
    codon, prot = content[0::2], content[1::2]
    codon_table = dict()

    for codon, prot in zip(codon, prot):
        codon_table[codon] = prot
    return codon_table


def xna_to_prot(xna):
    """Converts a DNA or mRNA string to protein"""
    prot = list()
    rna_table = {
        "UUU": "F",
        "CUU": "L",
        "AUU": "I",
        "GUU": "V",
        "UUC": "F",
        "CUC": "L",
        "AUC": "I",
        "GUC": "V",
        "UUA": "L",
        "CUA": "L",
        "AUA": "I",
        "GUA": "V",
        "UUG": "L",
        "CUG": "L",
        "AUG": "M",
        "GUG": "V",
        "UCU": "S",
        "CCU": "P",
        "ACU": "T",
        "GCU": "A",
        "UCC": "S",
        "CCC": "P",
        "ACC": "T",
        "GCC": "A",
        "UCA": "S",
        "CCA": "P",
        "ACA": "T",
        "GCA": "A",
        "UCG": "S",
        "CCG": "P",
        "ACG": "T",
        "GCG": "A",
        "UAU": "Y",
        "CAU": "H",
        "AAU": "N",
        "GAU": "D",
        "UAC": "Y",
        "CAC": "H",
        "AAC": "N",
        "GAC": "D",
        "UAA": "Stop",
        "CAA": "Q",
        "AAA": "K",
        "GAA": "E",
        "UAG": "Stop",
        "CAG": "Q",
        "AAG": "K",
        "GAG": "E",
        "UGU": "C",
        "CGU": "R",
        "AGU": "S",
        "GGU": "G",
        "UGC": "C",
        "CGC": "R",
        "AGC": "S",
        "GGC": "G",
        "UGA": "Stop",
        "CGA": "R",
        "AGA": "R",
        "GGA": "G",
        "UGG": "W",
        "CGG": "R",
        "AGG": "R",
        "GGG": "G",
    }

    xna = xna.upper()
    # Converts potential DNA string to RNA
    if "T" in xna:
        xna = xna.replace("T", "U")
    # Checks if there is a whole number of codons in xna
    try:
        remainder = len(xna) % 3
        if remainder != 0:
            raise ex.CodonRangeError(remainder)
    # If there isn't a whole number of codons, truncate the remainder
    # but warn the user
    except ex.CodonRangeError:
        print(f"{remainder} nucleotides truncated")
        xna = xna[:-remainder]
    # iterate through codon positions in xna, appending amino acids
    for codon_start in range(0, len(xna), 3):
        codon = xna[codon_start : codon_start + 3]
        prot.append(rna_table[codon])
    # Truncate stop codons at the end of protein, if any. If 'Stop' is
    # somehow found in the middle of protein string, it is left there for
    # diagnosis
    if prot[-1] == "Stop":
        del prot[-1]

    prot_str = "".join(prot)

    return prot_str
