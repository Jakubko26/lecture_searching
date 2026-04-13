from random import choices


def unordered_sequence(max_len=100):
    return choices(range(-1000, 1000), k=max_len)


def ordered_sequence(max_len=100):
    return sorted(choices(range(-1000, 1000), k=max_len))


def dna_sequence(max_len=100):
    return "".join(choices("ACGT", k=max_len))

def linear_search(data, cil):
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

def main():
    nums = unordered_sequence(20)
    sorted_nums =ordered_sequence(20)
    dna = dna_sequence(100)

    print("Unsorted:", nums)
    print("Sorted:", sorted_nums)
    print("DNA:", dna)

    print("\nLinear search:", linear_search(nums, nums[3]))
    print("Binary search:", binar_search(sorted_nums, sorted_nums[5]))
    print("Pattern search:", pattern_search(dna, dna[10:15]))

if __name__ == "__main__":
    main()
