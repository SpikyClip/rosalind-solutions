# url: http://rosalind.info/problems/grph/

# Problem

# A graph whose nodes have all been labeled can be represented by an
# adjacency list, in which each row of the list contains the two node
# labels corresponding to a unique edge.

# A directed graph (or digraph) is a graph containing directed edges, each
# of which has an orientation. That is, a directed edge is represented by
# an arrow instead of a line segment; the starting and ending nodes of an
# edge form its tail and head, respectively. The directed edge with tail v
# and head w is represented by (v,w) (but not by (w,v)). A directed loop
# is a directed edge of the form (v,v).

# For a collection of strings and a positive integer k, the overlap graph
# for the strings is a directed graph Ok in which each string is
# represented by a node, and string s is connected to string t with a
# directed edge when there is a length k suffix of s that matches a length
# k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops
# in the overlap graph (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length
# at most 10 kbp.

# Return: The adjacency list corresponding to O3. You may return edges in
# any order.

from common import fasta_to_dict


def adj_list(seq_dict, k):
    """Returns an adjacency list of tuples from a dictionary of sequences
    with a given adjacency length k"""

    adj_list = list()
    for name, seq in seq_dict.items():
        seq_dict[name] = (seq[:k], seq[-k:])
    # Cycles through each string's suffix, comparing it to all other
    # prefix's (except its own)
    for name_1, (_, suffix_1) in seq_dict.items():
        for name_2, (prefix_2, _) in seq_dict.items():
            if name_1 is name_2:
                continue
            else:
                if suffix_1 == prefix_2:
                    adj_list.append((name_1, name_2))

    return adj_list


if __name__ == "__main__":
    file1, file2 = "inputs/GRPH_input.txt", "outputs/GRPH_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        seq_dict = fasta_to_dict(f1.read())
        adj_list = adj_list(seq_dict, 3)
        for s, t in adj_list:
            f2.write(f"{s} {t}\n")