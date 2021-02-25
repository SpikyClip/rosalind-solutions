# url = http://rosalind.info/problems/mprt/

# Problem

# To allow for the presence of its varying forms, a protein motif is
# represented by a shorthand as follows: [XY] means "either X or Y" and
# {X} means "any amino acid except X." For example, the N-glycosylation
# motif is written as N{P}[ST]{P}.

# You can see the complete description and features of a particular protein
# by its access ID "uniprot_id" in the UniProt database, by inserting the
# ID number into

# http://www.uniprot.org/uniprot/uniprot_id

# Alternatively, you can obtain a protein sequence in FASTA format by
# following

# http://www.uniprot.org/uniprot/uniprot_id.fasta

# For example, the data for protein B5ZC00 can be found at

# http://www.uniprot.org/uniprot/B5ZC00.

# Given: At most 15 UniProt Protein Database access IDs.

# Return: For each protein possessing the N-glycosylation motif, output
# its given access ID followed by a list of locations in the protein
# string where the motif can be found.

from urllib.request import urlopen
from common import fasta_to_dict
import re


def url_to_str(url):
    """Opens a url leading to a text file as a string"""
    url_str = urlopen(url).read().decode("utf-8")

    return url_str


def main(uniprot_ids, motif):
    """
    Given a list of uniprot ids and a regex rawstring motif, pull protein
    sequences from uniprot and return a string of uniprot IDs that match
    regex motif along with locations where those motifs are found
    """
    motif = re.compile(motif)
    raw_input_list = list()
    output_list = list()

    # pulls raw data from uniprot into raw_input_list
    for uniprot_id in uniprot_ids:
        url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
        raw_input_list.append(url_to_str(url))

    # converts raw_input_list into dict
    compiled_raw_input = "".join(raw_input_list)
    seq_dict = fasta_to_dict(compiled_raw_input)

    # Rosalind wants uniprot_id as given, hence seq_dict.keys() not used
    for uniprot_id, protein in zip(uniprot_ids, seq_dict.values()):
        # uses regex to find motif, then returns match.start()+1 as
        # rosalind wants base 1 numbering
        indices = [str(match.start() + 1) for match in motif.finditer(protein)]
        # only appends indices if a match was found, i.e. indices not empty
        if indices:
            output_list.append(f"{uniprot_id}\n{' '.join(indices)}")

    # joins list to str ready for file write
    output_str = "\n".join(output_list)

    return output_str


if __name__ == "__main__":
    file1, file2 = "inputs/MPRT_input.txt", "outputs/MPRT_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        uniprot_ids = f1.read().splitlines()
        # uses lookahead assertion '?=' for motif to capture overlapping motifs
        f2.write(main(uniprot_ids, r"(?=N[^P][ST][^P])"))