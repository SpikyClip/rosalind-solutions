from common import fasta_to_dict


def adj_list(seq_dict, k):
    """Returns an adjacency list of tuples from a dictionary of sequences
    with a given adjacency length k"""

    adj_list = list()
    for name, seq in seq_dict.items():
        seq_dict[name] = (seq[:k], seq[-k:])
    # Cycles through each string's suffix, comparing it to all other
    # prefix's (except its own)
    for name_1, (prefix_1, suffix_1) in seq_dict.items():
        for name_2, (prefix_2, suffix_2) in seq_dict.items():
            if name_1 is name_2:
                continue
            else:
                if suffix_1 == prefix_2:
                    adj_list.append((name_1, name_2))

    return adj_list


if __name__ == "__main__":
    file1, file2 = "inputs/GRPH_input.txt", "outputs/GRPH_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        seq_dict = fasta_to_dict(f1)
        adj_list = adj_list(seq_dict, 3)
        for s, t in adj_list:
            f2.write(f"{s} {t}\n")