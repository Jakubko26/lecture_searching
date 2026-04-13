from random import choices


def unordered_sequence(max_len=100):
    return choices(range(-1000, 1000), k=max_len)


def ordered_sequence(max_len=100):
    return sorted(choices(range(-1000, 1000), k=max_len))


def dna_sequence(max_len=100):
    return "".join(choices("ACGT", k=max_len))


def main():
    print(unordered_sequence(max_len=500))
    print(ordered_sequence(max_len=500))
    print(dna_sequence(max_len=500))


if __name__ == "__main__":
    main()
