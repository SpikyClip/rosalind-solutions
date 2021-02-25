# url: http://rosalind.info/problems/cons/

# Problem

# A matrix is a rectangular table of values divided into rows and columns.
# An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j
# to indicate the value found at the intersection of row i and column j.

# Say that we have a collection of DNA strings, all having the same length
# n. Their profile matrix is a 4×n matrix P in which P1,j represents the
# number of times that 'A' occurs in the jth position of one of the strings,
# P2,j represents the number of times that C occurs in the jth position,
# and so on (see below).

# A consensus string c is a string of length n formed from our collection
# by taking the most common symbol at each position; the jth symbol of c
# therefore corresponds to the symbol having the maximum value in the j-th
# column of the profile matrix. Of course, there may be more than one most
# common symbol, leading to multiple possible consensus strings.

import numpy as np, pandas as pd

from common import fasta_to_dict


def cons_and_profile(strings):
    """Return a consensus string and profile matrix from a list of strings"""
    # converts seq to list of characters in preparation for array generation
    seq_list = [list(seq) for seq in strings]
    DNA_array = pd.DataFrame(seq_list)

    # value_counts applied to each column and na filled as zero
    profile_matrix = DNA_array.apply(pd.value_counts).fillna(0).astype("int32")

    # converts only row of DNA_array.mode() into string format
    cons_string = "".join(list(DNA_array.mode().iloc[0, :]))

    return cons_string, profile_matrix


if __name__ == "__main__":
    file1, file2 = "inputs/CONS_input.txt", "outputs/CONS_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        seq_dict = fasta_to_dict(f1.read())
        cons_string, profile_matrix = cons_and_profile(seq_dict.values())
        # insert colons into index
        profile_matrix.index = [i + ":" for i in profile_matrix.index]
        # converts profile_matrix to string format matrix profile without
        #  header and with single spacing between columns
        profile_matrix_str = profile_matrix.to_string(header=False).replace(
            "  ", " "
        )
        result = f"{cons_string}\n{profile_matrix_str}"
        f2.write(result)