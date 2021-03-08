# url: http://rosalind.info/problems/perm/

# Problem

# A permutation of length n is an ordering of the positive integers
# {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

# Given: A positive integer n≤7.

# Return: The total number of permutations of length n, followed by a
# list of all such permutations (in any order).

from itertools import permutations

if __name__ == "__main__":
    file1, file2 = "inputs/PERM_input.txt", "outputs/PERM_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        n = int(f1.read())
        numbers = [str(num) for num in range(1, n + 1)]
        perms = list(permutations(numbers))
        f2.write(f"{len(perms)}\n")
        for perm in perms:
            f2.write(f"{' '.join(perm)}\n")