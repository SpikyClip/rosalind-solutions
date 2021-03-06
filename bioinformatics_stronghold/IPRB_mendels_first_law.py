# url: http://rosalind.info/problems/iprb/

# Problem

# Given: Three positive integers k, m, and n, representing a totalulation
# containing k+m+n organisms: k individuals are homozygous dominant for a
# factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will
# produce an individual possessing a dominant allele (and thus displaying
# the dominant phenotype). Assume that any two organisms can mate.

from collections import Counter
from itertools import product, combinations, combinations_with_replacement

genotypes = [["A", "A"], ["A", "a"], ["a", "a"]]

possible_pairs = combinations_with_replacement(genotypes, 2)
possible_children = Counter()
for mother, father in possible_pairs:
    for child in product(mother, father):
        print(child)

test
print(possible_children)


def prob_dom_offspring(AA, Aa, aa):
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


# total_recessive_children = aa_aa + (aa_Aa * 0.5) + (Aa_Aa * 0.25)
# total_dominant_children = 1 - total_recessive_children

# print(total_dominant_children)