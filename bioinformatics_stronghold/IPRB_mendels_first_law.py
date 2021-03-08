# url: http://rosalind.info/problems/iprb/

# Problem

# Given: Three positive integers k, m, and n, representing a total population
# containing k+m+n organisms: k individuals are homozygous dominant for a
# factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will
# produce an individual possessing a dominant allele (and thus displaying
# the dominant phenotype). Assume that any two organisms can mate.


def prob_dom_offspring(AA, Aa, aa):
    """
    Given number of homozygous dominant, heterozygous, and recessive
    parents in a population, return the probability of two randomly selected
    parents producing a dominant child
    """
    total = AA + Aa + aa
    # probability of choosing both homozygous recessive parents ,
    # followed by recessive offspring probability
    P_aaaa = (aa / total) * ((aa - 1) / (total - 1))
    P_aa_aaaa = 1
    # probability of choosing one homozygous recessive and one
    # heterozygous parent, followed by recessive offspring probability
    P_aaAa = (aa / total) * (Aa / (total - 1)) + (Aa / total) * (
        aa / (total - 1)
    )
    P_aa_aaAa = 2 / 4
    # probability of choosing both heterozygous parents , followed by
    # recessive offspring probability
    P_AaAa = (Aa / total) * ((Aa - 1) / (total - 1))
    P_aa_AaAa = 1 / 4

    parent_prob = [P_aaaa, P_aaAa, P_AaAa]
    offspring_prob = [P_aa_aaaa, P_aa_aaAa, P_aa_AaAa]

    total_prob_aa_children = 0

    for P_parent, P_offspring in zip(parent_prob, offspring_prob):
        total_prob_aa_children += P_parent * P_offspring

    total_prob_AA_children = 1 - total_prob_aa_children

    return round(total_prob_AA_children, 5)


if __name__ == "__main__":
    file1, file2 = "inputs/IPRB_input.txt", "outputs/IPRB_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        AA, Aa, aa = [int(num) for num in f1.read().split()]
        f2.write(str(prob_dom_offspring(AA, Aa, aa)))
