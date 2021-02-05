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


def reverse_complement(seq):
    """Returns the reverse complement of a DNA nucleotide sequence"""
    complement_table = str.maketrans("ATCG", "TAGC")
    complement_seq = seq[::-1].translate(complement_table)
    return complement_seq


def patterncount(text, pattern):
    """Counts the number of times a pattern appears in text, returning count and
    list of starting positions as strings"""
    index = -1
    pattern_len = len(pattern)
    rev_pattern = reverse_complement(pattern)

    output = {
        "pattern_pos": [],
        "pattern_count": 0,
        "rev_pattern_pos": [],
        "rev_pattern_count": 0,
    }

    for i in range(len(text) - len(pattern)):
        frame = text[i : i + len(pattern)]

        if pattern in frame:
            output["pattern_count"] += 1
            output["pattern_pos"].append(i + 1)

        if rev_pattern in frame:
            output["rev_pattern_count"] += 1
            output["rev_pattern_pos"].append(i + 1)

    prev_pos = 0
    clusters = []
    for pos in output["pattern_pos"]:
        difference = pos - prev_pos
        if difference <= 9:
            clusters.append(prev_pos)
            clusters.append(pos)
        prev_pos = pos
    clusters = sorted(set(clusters))

    str_pattern_pos = " ".join([str(pos) for pos in output["pattern_pos"]])
    str_rev_pattern_pos = " ".join(
        [str(pos) for pos in output["rev_pattern_pos"]]
    )

    output[
        "printout"
    ] = f"""
    {pattern} count: {output['pattern_count']}
    {pattern} positions:
    {str_pattern_pos}\n
    {rev_pattern} count: {output['rev_pattern_count']}
    {rev_pattern} positions:
    {str_rev_pattern_pos}
    pattern clusters:
    {clusters}"""

    return output


pattern = "CTCCACTCT"
genome = """ACTCCACTGCGGACCTCCACTGCTCCACTTCACTCTCCACTCCTCCACTCTCCACTCTCCACTCTCCACTTGCTGGATTCTCCACTTGCCTCCACTTTTTGCTCCACTGCTCCACTTCCGTTACTCCACTCCTCCACTGGTCTGCTCCACTGACTCCACTATATGCTCCACTCCCATCTCCACTTCTCCACTCTCCACTCACTCCACTCTCCACTTCTCCACTCCCTCCACTAGTTCGCTCCACTCGCAGTGATCCACTCTCCACTCTCCACTCCCGCTCCACTGGCTCCACTCCTGCTCCACTCTCCACTGACTCCACTCTCCACTCTCCACTCCTCCACTTGATCTCCACTGCTCCACTCAGCTCCACTTACTCCACTCTCCACTCTCCACTCCTCCACTAAGCCTCCACTACCTCCACTCCTCCACTACCGTCTCCACTACCCTCCACTACCTCCACTATAGCTCCACTACAAGTACCTCCACTCGGCTCCACTCTCCACTCTCCACTTTTGAACCCGCTCCACTCTCCACTACGGGTCTCCACTCTTTGTCCTCCACTCCACTCCACTCTCCACTTCTCCACTCTTCTCCACTCTCCACTCTCCACTTCCTCCACTGGACTCCACTGCTCCACTCTCCACTTCCTCCACTTCTCCACTAGTCTCCACTTTCTCCACTAACTCCACTCTCCACTCTCCACTCTCCACTGCTCCACTACTCCACTTTACTCCACTAACATGTTGGGCTCCACTCTCCACTACTCCACTATGCCCTCCACTCACTCCACTCTCCACTAACTCCACTATCTCCACTGCTCCACTAGGCTCCACTTCTCCACTCTCCACTACTCCACT"""

ans = patterncount(genome, pattern)

print(ans["printout"])
