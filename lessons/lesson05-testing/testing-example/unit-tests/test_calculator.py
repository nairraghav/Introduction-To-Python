from src import calculator


def test_calculator_add_one_param():
    assert calculator.add(2) == 2


def test_calculator_add_no_param():
    assert calculator.add() == 0


def test_calculator_add_multiple_param():
    assert calculator.add(1, 2, 3, 4, 5) == 15


def test_calculator_subtract_one_param():
    assert calculator.subtract(2) == -2


def test_calculator_subtract_no_param():
    assert calculator.subtract() == 0


def test_calculator_subtract_multiple_param():
    assert calculator.subtract(1, 2, 3, 4, 5) == -15


def test_calculator_multiply_one_param():
    assert calculator.multiply(2) == 2


def test_calculator_multiply_no_param():
    assert calculator.multiply() == 1


def test_calculator_multiply_multiple_param():
    assert calculator.multiply(1, 2, 3, 4, 5) == 120


def test_calculator_divide_one_param():
    assert calculator.divide(1) == 1


def test_calculator_divide_no_param():
    assert calculator.divide() == 1


def test_calculator_divide_multiple_param():
    assert calculator.divide(1, 2, 3, 4, 5) == (1 / 2 / 3 / 4 / 5)
