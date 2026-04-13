from random import choices


def unordered_sequence(max_len=100):
    return choices(range(-1000, 1000), k=max_len)


def ordered_sequence(max_len=100):
    return sorted(choices(range(-1000, 1000), k=max_len))


def dna_sequence(max_len=100):
    return "".join(choices("ACGT", k=max_len))

def linera_search(data, cil):
    for i, x in enumerate(data):
        if x == cil:
            return i
    return -1


def main():
    print(unordered_sequence(max_len=500))
    print(ordered_sequence(max_len=500))
    print(dna_sequence(max_len=500))

def binar_search(data, cil):
    lava, prava = 0, len(data)
    while lava <= prava:
        stred = (lava + prava) // 2
        if data[stred] == cil:
            return stred
        elif data[stred] < cil:
            lava = stred +1
        else:
            prava = stred +1
    return -1
def pattern_search(text, pattern):
    pozice = []
    n, m = len(text), len(pattern)
    for i in range(n - m +1):
        if text[i:i + m] == pattern:
            pozice.append(i)
    return pozice


if __name__ == "__main__":
    main()
