# url: http://rosalind.info/problems/tran/

# For DNA strings s1 and s2 having the same length, their
# transition/transversion ratio R(s1,s2) is the ratio of the total
# number of transitions to the total number of transversions, where
# symbol substitutions are inferred from mismatched corresponding
# symbols as when calculating Hamming distance
# (see “Counting Point Mutations”).

# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

# Return: The transition/transversion ratio R(s1,s2).


def substitution_ratio(dna1, dna2):
    """
    Compares two dna strands for substitution events, classifying them
    and returning the ratio of transitions to transversions along with a list
    of tuples containing information about substitution position and type
    """
    subs = list()
    transitions = [("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")]
    # Iterates through both dna strands, testing substitution type if
    # a mismatch is detected
    for i, pair in enumerate(zip(dna1, dna2)):
        if pair[0] != pair[1]:
            if pair in transitions:
                subs.append((i, True))
            else:
                subs.append((i, False))

    _, subs_type = zip(*subs)

    # counts the number of transitions (True) to the number of
    # transversions (False) returning its ratio
    try:
        ratio = subs_type.count(True) / subs_type.count(False)
    except ZeroDivisionError:
        print(
            "ZeroDivisionError: ratio cannot be calculated as there are no transversion events."
        )
        return (None, subs)

    return round(ratio, 3), subs


from common import fasta_to_dict

if __name__ == "__main__":
    file1, file2 = "inputs/TRAN_input.txt", "outputs/TRAN_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        dna1, dna2 = fasta_to_dict(f1.read()).values()
        ratio, _ = substitution_ratio(dna1, dna2)
        f2.write(str(ratio))
