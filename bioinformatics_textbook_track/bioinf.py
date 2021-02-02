def patterncount(text, pattern):
    '''Counts the number of times a pattern and its reverse complement appears 
    in text, returning an output dictionary containing positions and counts'''
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
            output['pattern_pos'].append(str(i))

        if rev_pattern in frame:
            output['rev_pattern_count'] += 1
            output['rev_pattern_pos'].append(str(i))

    output['printout'] = f"""
    {pattern} count: {output['pattern_count']}
    {pattern} positions:
    {' '.join(output['pattern_pos'])}\n
    {rev_pattern} count: {output['rev_pattern_count']}
    {rev_pattern} positions:
    {' '.join(output['rev_pattern_pos'])}\n"""

    return output

def max_freq(text, frame_length):
    '''Finds the most frequent k-mer in text'''
    frames = {}
#generates frames that move by 1 letter increments, excluding ends which are 
#shorter than frame_length
    for i in range(len(text) - frame_length):
        frame = text[i:i + frame_length]
#adds frames to dictionary without producing duplicates
        if frame in frames:
            frames[frame] += 1
        elif frame not in frames:
            frames[frame] = 1
#Returns frames with the max frequency, even if there are multiple answers
    max_freq = max(frames.values())
    max_frames = []
    for frame, freq in frames.items():
        if freq == max_freq:
            max_frames.append(frame)
    return sorted(max_frames)

def reverse_complement(seq):
    '''Returns the reverse complement of a DNA nucleotide sequence'''
    complement_table = str.maketrans('ATCG','TAGC')
    complement_seq = seq[::-1].translate(complement_table)
    return complement_seq

def clump_finder(genome, pattern_len, clump_window_len, pattern_freq):
    '''Returns all distinct k-mers forming (L, t)-clumps in genome as a 
    dictionary with index positions'''

    output = {}

#slides a 'clump' window over the genome, one nucleotide at a time, excluding
# the end of the genome that is shorter than the 'clump' window
    for i in range(len(genome) - clump_window_len + 1):
        clump_window = genome[i:i + clump_window_len]

#Within the 'clump' window, slides another 'frame' window to identify k-mers
        for n in range(len(clump_window) - pattern_len + 1):
            frame = clump_window[n:n + pattern_len]

#If k-mer occurs more than or equal to pattern frequency threshold that defines
#a clump, it is added to the output dict and the starting position (index) 
#recorded in a list
            if clump_window.count(frame) >= pattern_freq:
                index = i + n
                if frame in output:
                    output[frame].append(index)
                elif frame not in output:
                    output[frame] = [index]

    return output

def hammingdistance(sequenceA, sequenceB):
    point_mutations = 0
    for i in range(len(sequenceA)):
        if sequenceA[i] != sequenceB[i]:
            point_mutations += 1

    return point_mutations