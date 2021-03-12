from math import log10


def gc_match_prob(dna, gc_content):
    """Returns the common logarithm of the probability that a
    random string of len(dna) with a particular GC content
    will match 'dna' exactly"""

    at = dna.count("A") + dna.count("T")
    cg = dna.count("C") + dna.count("G")
    # given a gc content, the probability of getting A or T in a random
    # string is 1 - gc_content, divided by two. The same principle applies
    # to getting the probability of gc (just divide by two). This is exponentiated
    # to the frequencies of getting the respective characters, lumped together
    # since the probabilities of complementary nucleotides are the same
    prob = (((1 - gc_content) / 2) ** at) * ((gc_content / 2) ** cg)

    return round(log10(prob), 3)


if __name__ == "__main__":
    file1, file2 = "inputs/PROB_input.txt", "outputs/PROB_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        dna, gc_contents = f1.read().splitlines()
        gc_list = [float(gc) for gc in gc_contents.split()]
        prob_match = [gc_match_prob(dna, gc) for gc in gc_list]
        for prob in prob_match:
            f2.write(f"{prob} ")