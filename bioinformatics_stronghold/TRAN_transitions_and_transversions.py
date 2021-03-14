# url: http://rosalind.info/problems/tran/

# For DNA strings s1 and s2 having the same length, their
# transition/transversion ratio R(s1,s2) is the ratio of the total
# number of transitions to the total number of transversions, where
# symbol substitutions are inferred from mismatched corresponding
# symbols as when calculating Hamming distance
# (see “Counting Point Mutations”).

# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

# Return: The transition/transversion ratio R(s1,s2).


def transit_or_transvers(nuc1, nuc2):
    """
    Classifies corresponding nucleotides to its type, returning True
    if both are in the same type (transitions) or False if in different
    types (transversions)
    """

    # Catches potential non-substitutions
    if nuc1 == nuc2:
        raise ValueError("Both nucleotides are the same (no substitution)")

    nuc_dict = {"purines": ("A", "G"), "pyrimidines": ("C", "T")}

    nuc_identity = list()
    # classifies nuc to type
    for nuc in (nuc1, nuc2):
        for base_type, bases in nuc_dict.items():
            if nuc in bases:
                nuc_identity.append(base_type)
                break

    subs_type = {"transition": True, "transversion": False}

    nuc1, nuc2 = nuc_identity

    # classifies substitution event
    if nuc1 == nuc2:
        return subs_type["transition"]
    elif nuc1 != nuc2:
        return subs_type["transversion"]


def transit_transvers_ratio(dna1, dna2):
    """
    Compares two dna strands for substitution events, classifying them
    and returning the ratio of transitions to transversions along with a list
    of tuples containing information about substitution position and type
    """
    subs = list()
    # Iterates through both dna strands, testing substitution type if
    # a mismatch is detected
    for i, (nuc1, nuc2) in enumerate(zip(dna1, dna2)):
        if nuc1 != nuc2:
            subs_type = transit_or_transvers(nuc1, nuc2)
            subs.append((i, subs_type))

    _, subs_type = zip(*subs)

    # counts the number of transitions (True) to the number of
    # transversions (False) returning its ratio
    try:
    ratio = subs_type.count(True) / subs_type.count(False)
    except ZeroDivisionError:
        print("ZeroDivisionError: ratio cannot be calculated as there are no transversion events.")
        return (None, subs)

    return round(ratio, 3), subs


from common import fasta_to_dict

if __name__ == "__main__":
    file1, file2 = "inputs/TRAN_input.txt", "outputs/TRAN_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        dna1, dna2 = fasta_to_dict(f1.read()).values()
        ratio, _ = transit_transvers_ratio(dna1, dna2)
        f2.write(str(ratio))
