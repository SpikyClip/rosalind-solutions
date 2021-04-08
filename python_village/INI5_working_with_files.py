# url: http://rosalind.info/problems/ini5/

# Problem

# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file.
# Assume 1-based numbering of lines.


if __name__ == "__main__":
    file1, file2 = "inputs/INI5_input.txt", "outputs/INI5_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        even_lines = [line for line in f1.readlines()[1::2]]
        f2.write("".join(even_lines))