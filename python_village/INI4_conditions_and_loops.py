# url: http://rosalind.info/problems/ini4/

# Problem

# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.


def sum_odd(a, b):
    odd_int = list()
    for i in range(a, b + 1):
        if i % 2 != 0:
            odd_int.append(i)
    return sum(odd_int)


if __name__ == "__main__":
    file1, file2 = "inputs/INI4_input.txt", "outputs/INI4_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        a, b = [int(num) for num in f1.read().split()]
        f2.write(str(sum_odd(a, b)))