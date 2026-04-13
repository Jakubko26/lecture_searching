from pathlib import Path
import json
import time
import random
import matplotlib.pyplot as plt
from generators import linear_search, binar_search,unordered_sequence, ordered_sequence, pattern_search

def read_data(file_name, field):
    file_cesta = Path.cwd() / file_name

    if not file_cesta.exists():
        return None
    with open(file_cesta, "r", encoding="utf=8") as subor:
        data = json.load(subor)
    return data.get(field,None)
def measure(func, *args, repeat=5):
    total = 0

    for _ in range(repeat):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        total  += (end - start)
    return total / repeat

def main():
    data = read_data("sequential.json", "unordered_numbers")
    sorted_data = read_data("sequential.json", "ordered_numbers")
    dna = read_data("sequential.json", "dna_sequence")

    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []
    set_times = []

    for n in sizes:
        sample = data[:min(n, len(data))]
        sorted_sample = sorted_data[:min(n, len(sorted_data))]

        target = sample[len(sample) // 2]
        s = set(sample)

        linear_times.append(measure(linear_search, sample, target))
        binary_times.append(measure(binar_search, sorted_sample, target))
        set_times.append(measure(pattern_search, s, target))

        print(f"Hotovo n = {n}")
    plt.plot(sizes, linear_times, label="Linear search")
    plt.plot(sizes, binary_times, label="Binar search")
    plt.plot(sizes, set_times, label="Pattern search")

    plt.xlabel("Veľkosť vstupu")
    plt.ylabel("Čas (sekundy)")
    plt.title("Porovnanie algoritmov vyhľadávania")
    plt.legend()

    plt.show()
    unordered = read_data("sequential.json", "unordered_numbers")
    ordered = read_data("sequential.json", "ordered_numbers")
    dna = read_data("sequential.json", "dna_sequence")

    print("Unordered numbers:", unordered()[:10] if unordered() else None)
    print("Ordered numbers:", ordered[:10] if ordered else None)
    print("DNA:", dna[:50] if dna else None)

if __name__ == ("__main__"):
    main()


