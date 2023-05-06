from src.add import add_two_numbers, add_three_numbers


def main():
    a = 1
    b = 2
    c = 3

    result = add_two_numbers(a, b)
    print(f"{a} + {b} = {result}")

    result = add_three_numbers(a, b, c)
    print(f"{a} + {b} + {c} = {result}")


if __name__ == "__main__":
    main()
