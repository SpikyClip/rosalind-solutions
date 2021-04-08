# url: http://rosalind.info/problems/ini2/

# Problem

# given: two postive integers, a and b, each less than 1000
# return: The integer corresponding to square of the hypotenuse of the right
# triangle whose legs have lengths a and b


def hypotenuse(side_a, side_b):
    hypo_square = side_a ** 2 + side_b ** 2
    return hypo_square


if __name__ == "__main__":
    file1, file2 = "inputs/INI2_input.txt", "outputs/INI2_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        a, b = [int(side) for side in f1.read().split()]
        f2.write(str(hypotenuse(a, b)))
