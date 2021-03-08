# url: http://rosalind.info/problems/pper/

# Problem

# A partial permutation is an ordering of only k objects taken from a
# collection containing n objects (i.e., k≤n). For example, one partial
# permutation of three of the first eight positive integers is given by
# (5,7,2).

# The statistic P(n,k) counts the total number of partial permutations of
# k objects that can be formed from a collection of n objects. Note that
# P(n,n) is just the number of permutations of n objects, which we found
# to be equal to n!=n(n−1)(n−2)⋯(3)(2) in “Enumerating Gene Orders”.

# Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

# Return: The total number of partial permutations P(n,k), modulo 1,000,000.

from scipy.special import perm

if __name__ == "__main__":
    file1, file2 = "inputs/PPER_input.txt", "outputs/PPER_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        n, k = [int(num) for num in f1.read().split()]
        total = int(perm(n, k) % 1_000_000)
        f2.write(str(total))