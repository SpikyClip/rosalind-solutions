# url: http://rosalind.info/problems/revp/

# Problem

# A DNA string is a reverse palindrome if it is equal to its reverse
# complement. For instance, GCATGC is a reverse palindrome because its
# reverse complement is GCATGC.

# Given: A DNA string of length at most 1 kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the
# string having length between 4 and 12. You may return these pairs in
# any order.

from common import fasta_to_dict, rev_complement


def find_reverse_palindromes(dna, max_len):
    """
    Searches for palindromes in a DNA string given a max_length,
    Returning a list of tuples with index, length and palindrome. This
    function returns all nested palindromes.
    """

    if max_len % 2 != 0:
        raise ValueError("DNA can only have even length palindromes")

    palindromes = list()

    for i in range(len(dna)):
        for half_len in range(2, int(max_len / 2) + 1):
            # Checks if current position is long enough to have specified
            # palindrome half_len, else break
            if i >= half_len and len(dna[i:]) >= half_len:
                forward_back = dna[i - half_len : i]
                rev_front = rev_complement(dna[i : i + half_len])
                # Checks if dna slice is a palindrome, if so, setting
                # its value to current pal in consideration that it
                # might be part of a longer palindrome
                if forward_back == rev_front:
                    current_pal = (
                        i - half_len,
                        half_len * 2,
                        dna[i - half_len : i + half_len],
                    )
                    palindromes.append(current_pal)
                # escapes testing longer palindromes if shorter
                # palindromes aren't found
                else:
                    break

    # sorted by starting index
    return sorted(palindromes, key=lambda pal: pal[0])


if __name__ == "__main__":
    file1, file2 = "inputs/REVP_input.txt", "outputs/REVP_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        dna = list(fasta_to_dict(f1.read()).values())[0]
        palindromes = find_reverse_palindromes(dna, 12)
        for pos, len, _ in palindromes:
            f2.write(f"{pos+1} {len}\n")
