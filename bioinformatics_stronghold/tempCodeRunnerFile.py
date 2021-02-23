if __name__ == "__main__":
    file1, file2 = "inputs/IEV_input.txt", "outputs/IEV_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        freq = [int(freq) for freq in f1.read().split()]
        pairs = [
            ("AA", "AA"),
            ("AA", "Aa"),
            ("AA", "aa"),
            ("Aa", "Aa"),
            ("Aa", "aa"),
            ("aa", "aa"),
        ]
        f2.write(str(main(pairs, freq))