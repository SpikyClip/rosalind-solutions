from itertools import combinations


def fasta_to_dict(filename):
    """Converts fasta format from txt to dictionary"""
    seq_dict = dict()
    with open(filename) as f:
        # iterates by line in file for efficiency
        for line in f:
            # identifies fasta titles by '>' char, stripping '>' and
            # storing as seq_name to allow later reference to dict when
            # concatenating sequence.
            # seq_name also stored as key in dictionary with empty string
            # to allow for concatenation later
            if line.startswith(">"):
                seq_name = line.strip(">\n")
                seq_dict[seq_name] = ""
            # concatenates seq to current seq_name value in dict
            else:
                seq_dict[seq_name] += line.strip()

    return seq_dict


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
    main("LCSM_finding_shared_motif.txt")
