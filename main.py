def main():
    print("Hello from pondeli134!")


if __name__ == "__main__":
    main()

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Data:", sequential_data)

    target_number = 3

    result = linear_search(sequential_data, target_number)

    print("Hledané číslo:", target_number)
    print("Výsledek:", result)


if __name__ == "__main__":
    main()