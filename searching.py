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
def read_data(file_name, field):
    with open(file_name, "r", encoding="utf-8"):
        data = json.load(file_name)
    if field == "dna_sequence":
        return str(data)
    elif field == "ordered_numbers":
        return list(data)
    elif field == "unordered_numbers":
        return list(data)
    else:
        return None

#ukol2

