def number_to_pattern(index,pattern_len):
    '''Converts an index number for k-mer of giving length to its corresponding
    pattern'''

    pattern = ''
    letter_value = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

    # Starts reconstructing the symbols from the last letter of the k-mer
    for i in range(pattern_len):
        quotient = index // 4
    # value for remainder corresponds to the letter_value of the last symbol
        remainder = index % 4
        symbol = letter_value[remainder]
        pattern = symbol + pattern
    # quotient becomes the next index for the following iteration
        index = quotient

    return pattern

print(number_to_pattern(5246, 9))