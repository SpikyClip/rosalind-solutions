class CodonRangeError(IndexError):
    """
    Exception raised when a nucleotide string leads to imperfect
    number of codons
    """

    def __init__(self, remainder):
        message = f"Imperfect no. of codons, {remainder} nucleotides remaining."
        super().__init__(message)