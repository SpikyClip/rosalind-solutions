def pattern_to_number(pattern):
    """Converts a DNA nucleotide pattern into its index value in a alphabetical list
    of all possible k-mers of that length

    E.g. for pattern TGC

    3 loops, one for each nucleotide working backwards

    1st loop (C) counts the number of TG[X] that exist before TGC
    value of C is 1 indicating 1 nucleotide before C (A), only TGA in this set

    no. of loop 1 3-mers = 1 * 4^0 = 1 * 1 = 1

    2nd loop (G) counts the number of T[X][X] that exist before TG[A]. Two letters
    come before G (A, C) and TA[X] and TC[X] each have 4 possible 3-mers

    no. of loop 2 3-mers = 2 * 4^1 = 2 * 4 = 8

    3rd loop (T) counts all 3mers that exist before the starting letter T. As there
    are 3 such letters (A, C, G) and each starting letter has a set of 4^2
    combinations after it, the number of k-mers in this set is 

    no. of loop 3 3-mers = 3 * 4^2 = 3 * 16 = 48

    """

    letter_value = {'A':0, 'C':1, 'G':2, 'T':3}

    total = 0

    # iterates backwards from last letter in pattern
    for i in range (len(pattern)):
        rear_symbol = pattern[-(i+1)]

    # adds k-mers in each set to running total
        total += letter_value[rear_symbol] * len(letter_value) ** (i)

    return total

ans = pattern_to_number('TGC')

print(ans)
