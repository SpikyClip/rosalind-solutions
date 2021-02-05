# url: http://rosalind.info/problems/subs/

# Problem

# Given two strings s and t, t is a substring of s if t is contained as a
# contiguous collection of symbols in s (as a result, t must be no longer
# than s).

# The position of a symbol in a string is the total number of symbols found
# to its left, including itself (e.g., the positions of all occurrences of
# 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol
# at position i of s is denoted by s[i].

# A substring of s can be represented as s[j:k], where j and k represent
# the starting and ending positions of the substring in s; for example, if
# s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

# The location of a substring s[j:k] is its beginning position j; note that
# t will have multiple locations in s if it occurs more than once as a
# substring of s (see the Sample below).

# Given: Two DNA strings s and t (each of length at most 1 kbp).

# Return: All locations of t as a substring of s.

from common import rev_complement


def substr_index(string, substring):
    """Returns a list of indices where substring occurs in string"""
    index = []
    for i in range(len(string)):
        if string[i:].startswith(substring):
            index.append(i)
    if index:
        return index
    else:
        return None


if __name__ == "__main__":
    file1, file2 = "inputs/009_SUBS_input.txt", "outputs/009_SUBS_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        string, substring = f1.read().splitlines()
        # adds +1 to indice to meet rosalind requirements
        result = [str(i + 1) for i in substr_index(string, substring)]
        f2.write(" ".join(result))
