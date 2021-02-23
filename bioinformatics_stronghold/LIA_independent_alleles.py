# url: http://rosalind.info/problems/lia/

# Problem
# Figure 2. The probability of each outcome for the sum of the values on
# two rolled dice (black and white), broken down depending on the number
# of pips showing on each die. You can verify that 18 of the 36 equally
# probable possibilities result in an odd sum.

# Two events A and B are independent if Pr(A and B) is equal to Pr(A)×Pr(B).
# In other words, the events do not influence each other, so that we may
# simply calculate each of the individual probabilities separately and
# then multiply.

# More generally, random variables X and Y are independent if whenever A
# and B are respective events for X and Y, A and B are independent
# (i.e., Pr(A and B)=Pr(A)×Pr(B)).

# As an example of how helpful independence can be for calculating
# probabilities, let X and Y represent the numbers showing on two six-sided
# dice. Intuitively, the number of pips showing on one die should not
# affect the number showing on the other die. If we want to find the
# probability that X+Y is odd, then we don't need to draw a tree diagram
# and consider all possibilities. We simply first note that for X+Y to be
# odd, either X is even and Y is odd or X is odd and Y is even. In terms
# of probability, Pr(X+Y is odd)=Pr(X is even and Y is odd)+Pr(X is odd
# and Y is even). Using independence, this becomes [Pr(X is even)×Pr(Y is
# odd)]+[Pr(X is odd)×Pr(Y is even)], or (12)2+(12)2=12. You can verify
# this result in Figure 2, which shows all 36 outcomes for rolling two dice.

# Given: Two positive integers k(k≤7) and N (N≤2k). In this problem, we
# begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has
# two children in the 1st generation, each of whom has two children, and
# so on. Each organism always mates with an organism having genotype Aa Bb.

# Return: The probability that at least N Aa Bb organisms will belong to
# the k-th generation of Tom's family tree (don't count the Aa Bb mates at
# each level). Assume that Mendel's second law holds for the factors.

from math import gcd
from itertools import product
from scipy.stats import binom


def offspring_ratio(allele_1, allele_2):
    """
    Returns the ratio of possible offspring genotypes for a single gene
    as a tuple given the genotype of one parent (True=Dominant, False=
    Recessive) mating with all possible combinations of genotypes
    """
    parent_1 = (allele_1, allele_2)
    possible_parent_2 = [(True, True), (True, False), (False, False)]
    hom_dom, het, hom_rec = 0, 0, 0

    for parent_2 in possible_parent_2:
        for offspring in product(parent_1, parent_2):

            if all(offspring):
                hom_dom += 1
            elif not any(offspring):
                hom_rec += 1
            else:
                het += 1
    # obtains the greatest common divisor for ratio to return a
    # simplified ratio
    ratio = (hom_dom, het, hom_rec)
    div = gcd(*ratio)
    ratio = tuple(int(num / div) for num in ratio)

    return ratio


def offspring_prob(offspring_ratio):
    """
    Returns the probabilities of obtaining offspring genotypes as a
    tuple given the offspring ratio as a tuple
    """
    prob = tuple(num / sum(offspring_ratio) for num in offspring_ratio)

    return prob


def prob_least_n_genotype(generation, n, probability):
    """
    Returns the probability that at least n individuals of a particular
    genotype associated with a offspring probability are found at a
    particular generation
    """
    # the population of a particular generation given each parent
    # produces 2 offspring is 2 to the power of the generation number
    # the probability of at least n individuals is the sum of all
    # probabilities (1) minus the cumulative binomial probability of
    # obtaining n-1 or less individuals
    gen_pop = 2 ** generation
    prob_least_n_genotype = 1 - binom.cdf(n - 1, gen_pop, probability)

    return round(prob_least_n_genotype, 3)


if __name__ == "__main__":
    # proves the 0.5 probability of getting a heterozygous outcome
    # empirically, but analytically it is always 0.5 as long as one
    # parent is heterozygous
    ratio = offspring_ratio(True, False)
    # offspring_prob is squared, as two genes are involved and both
    # segregate independently
    het_prob = offspring_prob(ratio)[1] ** 2

    file1, file2 = "inputs/LIA_input.txt", "outputs/LIA_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        generation, n = (int(value) for value in f1.read().split())
        prob_least_n_genotype = prob_least_n_genotype(generation, n, het_prob)
        f2.write(str(prob_least_n_genotype))