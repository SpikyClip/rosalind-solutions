import numpy as np
import pandas as pd

filename = "CONS_in.txt"
seq_dict = dict()

# opens file as list of lines without \n chars
with open(filename) as f:
    line_list = f.read().splitlines()

# parses line_list, storing names and seq in seq_dict
for line in line_list:
    if line.startswith(">"):
        seq_name = line.lstrip(">")
        seq_dict[seq_name] = ""
    else:
        seq_dict[seq_name] += line

# converts seq to list of characters in preparation for array generation
seq_list = [list(seq) for seq in seq_dict.values()]

DNA_array = pd.DataFrame(seq_list)

cons_DNA_array = DNA_array.apply(pd.value_counts).fillna(0).astype("int32")
cons_DNA_array.index = [i + ":" for i in cons_DNA_array.index]

# converts only row of DNA_array.mode() into string format
cons_string = "".join(list(DNA_array.mode().iloc[0, :]))

# converts cons_DNA_array to string format matrix profile without header
# and with single spacing between columns
cons_matrix_profile = cons_DNA_array.to_string(header=False).replace("  ", " ")

output = f"{cons_string}\n{cons_matrix_profile}"

# writes output to file
with open("CONS_out.txt", "w") as f:
    f.write(output)