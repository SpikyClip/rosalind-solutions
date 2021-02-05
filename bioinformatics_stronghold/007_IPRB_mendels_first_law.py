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


print(possible_children)


# AA, Aa, aa = 19, 20, 15
# total = AA + Aa + aa

# aa_aa = (aa / total) * ((aa - 1) / (total - 1))
# aa_Aa = (aa / total) * (Aa / (total - 1)) + (Aa / total) * (
#     aa / (total - 1)
# )
# Aa_Aa = (Aa / total) * ((Aa - 1) / (total - 1))

# total_recessive_children = aa_aa + (aa_Aa * 0.5) + (Aa_Aa * 0.25)
# total_dominant_children = 1 - total_recessive_children

# print(total_dominant_children)