# example.py
# This code asks you for your name and prints a Hello


def get_name_from_input():
    while True:
        name = input("What is your name? ")
        if len(name.strip()) != 0:
            return name


def print_name(name):
    print(f"Hello {name}!")


if __name__ == "__main__":
    print_name(get_name_from_input())