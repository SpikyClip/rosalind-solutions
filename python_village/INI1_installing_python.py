# url: http://rosalind.info/problems/ini1/

# Problem

# After downloading and installing Python, type import this into the
# Python command line and see what happens. Then, click the "Download
# dataset" button below and copy the Zen of Python into the space
# provided.

from this import s

# This is not really necessary, but thought it was interesting to break
# down what 'this.py' was doing in the background

d = {}
# C is the integer that starts unicode uppercase A and lowercase a
for c in (65, 97):
    # cycles through alphabet order
    for i in range(26):
        # i + c creates keys associated with all upper/lower unicode
        # alphabet. RHS returns decoded ROT13, 'i + 13' displaces
        # characters by 13 letters, '% 26' allows it to wrap around the
        # cipher, and '+c' ensures the correct case
        d[chr(i + c)] = chr((i + 13) % 26 + c)

# List comprehension joined into a string. Ciphered letters in s are
# used to fetch their decoded values from the dictionary.
# 'dict.get(c,c)' is used to ignore characters in s that are not word
# characters, which are not present in the dictionary
zen = "".join([d.get(c, c) for c in s])

if __name__ == "__main__":
    file = "outputs/INI1_output.txt"
    with open(file, "w") as f:
        f.write(zen)
