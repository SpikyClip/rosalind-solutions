# url: http://rosalind.info/problems/lcsm/

# Problem

# A common substring of a collection of strings is a substring of every
# member of the collection. We say that a common substring is a longest
# common substring if there does not exist a longer common substring.
# For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA",
# but it is not as long as possible; in this case, "CGTA" is a longest
# common substring of "ACGTACGT" and "AACCGTATA".

# Note that the longest common substring is not necessarily unique; for
# a simple example, "AA" and "CC" are both longest common substrings of
# "AACC" and "CCAA".

# Given: A collection of k(k≤100) DNA strings of length at most 1 kbp
# each in FASTA format.

# Return: A longest common substring of the collection. (If multiple
# solutions exist, you may return any single solution.)

from itertools import combinations
from common import fasta_to_dict


def longest_common_motif(seq_list):
    """Returns a list of the longest substrings found in all strings in seq_list"""
    # sorts seq_list to find shortest string, as the longest possible
    # substring cannot exceed length of shortest string
    sorted_seqs = sorted(seq_list, key=len)
    shortest_seq, *remaining_seqs = sorted_seqs
    n = len(shortest_seq)
    longest_common_motif = []
    found = False
    # generates all possible substring slice indices as a list of tuples
    substr_indices = [(i, j) for i, j in combinations(range(n + 1), 2)]
    # sorts substr_indices by slice length in descending order. This is
    # done so that iterating over substr_indices will evaluate
    # progressively shorter substrings, allowing us to end our search
    # as soon as a longest common motif is found and all further
    # substrings are shorter or equal in length to the longest common
    # motif found
    substr_indices.sort(key=lambda tup: tup[1] - tup[0], reverse=True)

    # loops through substr_indices and generates a test_motif as a slice
    # of the shortest_seq. More efficient than generating all possible
    # slices, as we can stop as soon as the longest common motif is found
    for start, stop in substr_indices:
        test_motif = shortest_seq[start:stop]
        # if longest common motif was found in a previous iteration, the
        # only reason to continue testing is if there are remaining
        # substrings of equal length. If test_motif is shorter, break
        # the loop.
        if found and (len(test_motif) < len(longest_common_motif[0])):
            break
        # uses a generator comprehension, checking if test_motif is in
        # remaining_seqs. all() ends the generator immediately if False
        # is returned, avoiding the need to check all sequences unless
        # test_motif is in all sequences
        in_all = all(test_motif in seq for seq in remaining_seqs)
        # found flag set to True to account for first discovery of
        # longest common motif. test_motif is appended to consider
        # possibility of multiple longest common motifs with equal length
        if in_all:
            found = True
            longest_common_motif.append(test_motif)

    return longest_common_motif


def main(filename):
    seq_list = list(fasta_to_dict(filename).values())
    motif_list = longest_common_motif(seq_list)
    for motif in motif_list:
        print(motif)


if __name__ == "__main__":
    file1, file2 = "inputs/LCSM_input.txt", "outputs/LCSM_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        seq_list = list(fasta_to_dict(f1.read()).values())
        motif_list = longest_common_motif(seq_list)
        f2.write(motif_list[0])