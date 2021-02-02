from bioinf import reverse_complement

def patterncount(text, pattern):
    '''Counts the number of times a pattern appears in text, returning count and
    list of starting positions as strings'''
    index = -1
    pattern_len = len(pattern)
    rev_pattern = reverse_complement(pattern)

    output = {
    'pattern_pos':[],
    'pattern_count': 0,
    'rev_pattern_pos': [],
    'rev_pattern_count': 0,
    }

    for i in range(len(text) - len(pattern)):
        frame = text[i:i + len(pattern)]

        if pattern in frame:
            output['pattern_count'] += 1
            output['pattern_pos'].append(i)

        if rev_pattern in frame:
            output['rev_pattern_count'] += 1
            output['rev_pattern_pos'].append(i)

    prev_pos = 0
    clusters = []
    for pos in output['pattern_pos']:
        difference = pos - prev_pos
        if difference <= 9:
            clusters.append(prev_pos)
            clusters.append(pos)
        prev_pos = pos
    clusters = sorted(set(clusters))

    str_pattern_pos = ' '.join([str(pos) for pos in output['pattern_pos']])
    str_rev_pattern_pos = ' '.join([str(pos) for pos in output['rev_pattern_pos']])

    output['printout'] = f"""
    {pattern} count: {output['pattern_count']}
    {pattern} positions:
    {str_pattern_pos}\n
    {rev_pattern} count: {output['rev_pattern_count']}
    {rev_pattern} positions:
    {str_rev_pattern_pos}
    pattern clusters:
    {clusters}"""

    return output

pattern = 'CTCCACTCT'
genome = '''ACTCCACTGCGGACCTCCACTGCTCCACTTCACTCTCCACTCCTCCACTCTCCACTCTCCACTCTCCACTTGCTGGATTCTCCACTTGCCTCCACTTTTTGCTCCACTGCTCCACTTCCGTTACTCCACTCCTCCACTGGTCTGCTCCACTGACTCCACTATATGCTCCACTCCCATCTCCACTTCTCCACTCTCCACTCACTCCACTCTCCACTTCTCCACTCCCTCCACTAGTTCGCTCCACTCGCAGTGATCCACTCTCCACTCTCCACTCCCGCTCCACTGGCTCCACTCCTGCTCCACTCTCCACTGACTCCACTCTCCACTCTCCACTCCTCCACTTGATCTCCACTGCTCCACTCAGCTCCACTTACTCCACTCTCCACTCTCCACTCCTCCACTAAGCCTCCACTACCTCCACTCCTCCACTACCGTCTCCACTACCCTCCACTACCTCCACTATAGCTCCACTACAAGTACCTCCACTCGGCTCCACTCTCCACTCTCCACTTTTGAACCCGCTCCACTCTCCACTACGGGTCTCCACTCTTTGTCCTCCACTCCACTCCACTCTCCACTTCTCCACTCTTCTCCACTCTCCACTCTCCACTTCCTCCACTGGACTCCACTGCTCCACTCTCCACTTCCTCCACTTCTCCACTAGTCTCCACTTTCTCCACTAACTCCACTCTCCACTCTCCACTCTCCACTGCTCCACTACTCCACTTTACTCCACTAACATGTTGGGCTCCACTCTCCACTACTCCACTATGCCCTCCACTCACTCCACTCTCCACTAACTCCACTATCTCCACTGCTCCACTAGGCTCCACTTCTCCACTCTCCACTACTCCACT'''

ans = patterncount(genome, pattern)

print(ans['printout'])