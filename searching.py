from dataclasses import field
from pathlib import Path
import json

#from pondeli134.generators import dna_sequence


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()

    file_path = cwd_path / file_name


#ukol1
import json


def read_data(filename, field):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        if field not in data:
            return None

        return data[field]

    except (FileNotFoundError, json.JSONDecodeError):
        return None

#ukol2
def linear_search(sequence, target):
    positions = []

    for index, value in enumerate(sequence):
        if value == target:
            positions.append(index)

    result = {
        "positions": positions,
        "count": len(positions)
    }

    return result

#ukol3
def binary_search(sequence, target):
    levacka = 0
    pravacka = len(sequence) - 1

    while levacka <= pravacka:
        mid = (levacka + pravacka) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            levacka = mid + 1
        else:
            pravacka = mid - 1

    return None

import matplotlib.pyplot as plt

# sizes = [100, 500, 1000, 5000, 10000]
# times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]
#
# plt.plot(sizes, times)

# plt.xlabel("Velikost vstupu")
# plt.ylabel("Čas [s]")
# plt.title("Ukázkový graf měření")
# plt.show()


#ukolmerenicasu
import random
import time

def generate_data(size):
    data = [random.randint(0, size) for _ in range(size)]
    return data

def main():
    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []
    set_times = []

    target = -1
    repeats = 50

    for size in sizes:
        data = generate_data(size)
        sorted_data = sorted(data)
        data_set = set(data)

        start = time.time()
        for _ in range(repeats):
            linear_search(data, target)
        end = time.time()
        linear_times.append((end - start) / repeats)

        start = time.time()
        for _ in range(repeats):
            binary_search(sorted_data, target)
        end = time.time()
        binary_times.append((end - start) / repeats)

        start = time.time()
        for _ in range(repeats):
            target in data_set
        end = time.time()
        set_times.append((end - start) / repeats)

    plt.figure()

    plt.plot(sizes, linear_times, label="Linear Search")
    plt.plot(sizes, binary_times, label="Binary Search")
    plt.plot(sizes, set_times, label="Set Membership")

    plt.xlabel("velikost vstupu")
    plt.ylabel("cas (s)")
    plt.title("porovnavani algoritmu")
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()
