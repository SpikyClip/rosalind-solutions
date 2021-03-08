# url: http://rosalind.info/problems/lexf/

# Problem

# Assume that an alphabet A has a predetermined order; that is, we write
# the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For
# instance, the English alphabet is organized as (A,B,…,Z).

# Given two strings s and t having the same length n, we say that s
# precedes t in the lexicographic order (and write s<Lext) if the first
# symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

# Given: A collection of at most 10 symbols defining an ordered alphabet,
# and a positive integer n(n≤10).

# Return: All strings of length n that can be formed from the alphabet,
# ordered lexicographically (use the standard order of symbols in the
# English alphabet).

from itertools import product

if __name__ == "__main__":
    file1, file2 = "inputs/LEXF_input.txt", "outputs/LEXF_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        alphabet, n = f1.read().splitlines()
        alphabet, n = alphabet.split(), int(n)

        for perm in product(alphabet, repeat=n):
            f2.write(f"{''.join(perm)}\n")