# url: http://rosalind.info/problems/ini6/

# Problem

# Given: A string s of length at most 10000 letters.

# Return: The number of occurrences of each word in s, where words are
# separated by spaces. Words are case-sensitive, and the lines in the
# output can be in any order.


def word_count(string):
    unique_words = set(string.split())
    count_dict = {word: string.count(word) for word in unique_words}
    return count_dict


if __name__ == "__main__":
    file1, file2 = "inputs/INI6_input.txt", "outputs/INI6_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        string = f1.read()
        count_dict = word_count(string)

        output = list()
        for word, count in count_dict.items():
            output.append(f"{word} {count}\n")

        f2.write("".join(output))
