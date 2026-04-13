from pathlib import Path
import json
import time
import random
import matplotlib.pyplot as plt

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
    unordered = read_data("sequential.json", "unordered_numbers")
    ordered = read_data("sequential.json", "ordered_numbers")
    dna = read_data("sequential.json", "dna_sequence")

    print("Unordered numbers:", unordered[:10] if unordered else None)
    print("Ordered numbers:", ordered[:10] if ordered else None)
    print("DNA:", dna[:50] if dna else None)

if __name__ == ("__main__"):
    main()


