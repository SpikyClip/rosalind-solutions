# url: http://rosalind.info/problems/iev/

# Problem

# For a random variable X taking integer values between 1 and n, the
# expected value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us
# a way of taking the long-term average of a random variable over a large
# number of trials.

# As a motivating example, let X be the number on a six-sided die. Over a
# large number of rolls, we should expect to obtain an average of 3.5 on
# the die (even though it's not possible to roll a 3.5). The formula for
# expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

# More generally, a random variable for which every one of a number of
# equally spaced outcomes has the same probability is called a uniform
# random variable (in the die example, this "equal spacing" is equal to 1).
# We can generalize our die example to find that if X is a uniform random
# variable with minimum possible value a and maximum possible value b, then
# E(X)=a+b2. You may also wish to verify that for the dice example, if Y
# is the random variable associated with the outcome of a second die roll,
# then E(X+Y)=7.

# Given: Six nonnegative integers, each of which does not exceed 20,000.
# The integers correspond to the number of couples in a population
# possessing each genotype pairing for a given factor. In order, the six
# given integers represent the number of couples having the following
# genotypes:

#     AA-AA
#     AA-Aa
#     AA-aa
#     Aa-Aa
#     Aa-aa
#     aa-aa

# Return: The expected number of offspring displaying the dominant
# phenotype in the next generation, under the assumption that every couple
# has exactly two offspring.

import itertools as it


def offspring_zygosity(parent_1, parent_2):
    """
    return the ratio of homozygous dominant, heterozygous, and homozygous
    recessive offspring given the genotype of both parents for a single
    gene.
    """
    genotype_1, genotype_2 = tuple(parent_1), tuple(parent_2)
    offspring = it.product(genotype_1, genotype_2)

    homozygous_dominant, heterozygous, homozygous_recessive = 0, 0, 0

    for allele_1, allele_2 in offspring:
        dominant = (allele_1.isupper(), allele_2.isupper())
        if all(dominant):
            homozygous_dominant += 1
        elif not any(dominant):
            homozygous_recessive += 1
        else:
            heterozygous += 1

    return (homozygous_dominant, heterozygous, homozygous_recessive)


def pr_dominant_offpring(offspring_zygosity):
    """Given offspring zygosity as a tuple (hd, ht, hr) return probability
    of offspring possessing dominant allele"""

    homozygous_dominant, heterozygous, homozygous_recessive = offspring_zygosity

    total = homozygous_dominant + heterozygous + homozygous_recessive
    dominant = homozygous_dominant + heterozygous

    pr_dominant = dominant / total

    return pr_dominant


def main(pairs, freq):
    """
    Returns the number of dominant offspring given a related list of
    pairings and frequencies
    """
    total_dominant_offspring = 0
    pr_dom = [
        pr_dominant_offpring(offspring_zygosity(parent_1, parent_2))
        for parent_1, parent_2 in pairs
    ]
    for freq, pr_dom in zip(freq, pr_dom):
        pair_offspring = freq * 2
        total_dominant_offspring += pr_dom * pair_offspring

    return total_dominant_offspring


if __name__ == "__main__":
    file1, file2 = "inputs/IEV_input.txt", "outputs/IEV_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        freq = [int(freq) for freq in f1.read().split()]
        pairs = [
            ("AA", "AA"),
            ("AA", "Aa"),
            ("AA", "aa"),
            ("Aa", "Aa"),
            ("Aa", "aa"),
            ("aa", "aa"),
        ]
        result = str(main(pairs, freq))
        f2.write(result)
