def main():
    print("Hello from pondeli134!")



def main():
    ordered_data = read_data("sequential.json", "ordered_numbers")
    print("Data:", ordered_data)

    target_number = 3

    result = binary_search(ordered_data, target_number)

    print("Hledané číslo:", target_number)
    print("Index:", result)


if __name__ == "__main__":
    main()