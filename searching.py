from dataclasses import field
from pathlib import Path
import json

from pondeli134.generators import dna_sequence


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


def main():
    pass


if __name__ == "__main__":
    main()

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
    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

