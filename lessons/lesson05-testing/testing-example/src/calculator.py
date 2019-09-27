# calculator.py
# This script handles simple arithmetic operations


def add(*args):
    """
    :param args: This represents the group of ints that are to be added
    :return: This returns the total sum of all numbers that were added
    """
    total = 0
    for arg in args:
        if type(arg) is int:
            total += arg
    return total


def subtract(*args):
    """
    :param args: This represents the group of ints that are to be subtracted
    :return: This returns the total difference of all numbers that were
    subtracted
    """
    total = 0
    for arg in args:
        if type(arg) is int:
            total -= arg
    return total


def multiply(*args):
    """
    :param args: This represents the group of ints that are to be multiplied
    :return: This returns the total product of all numbers that were multiplied
    """
    total = 1
    for arg in args:
        if type(arg) is int:
            total *= arg
    return total


def divide(*args):
    """
    :param args: This represents the group of ints that are to be divided
    :return: This returns the total number after all numbers are divided
    """
    total = 1
    for arg in args:
        if type(arg) is int:
            total /= arg
    return total
