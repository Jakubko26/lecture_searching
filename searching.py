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

sizes = [100, 500, 1000, 5000, 10000]
times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]

plt.plot(sizes, times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()
def main():
    data = read_data("sequential.json", "unordered_numbers")
    sorted_data = read_data("sequential.json", "ordered_numbers")
    dna = read_data("sequential.json", "dna_sequence")

    sizes = [100, 500, 1000, 5000, 10000]


    plt.plot(sizes, linear_search(), label="Linear search")
    plt.plot(sizes, binary_s   , label="Binar search")
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


