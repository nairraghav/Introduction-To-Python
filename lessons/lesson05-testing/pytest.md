# Testing

## Why Test?
The main benefit of writing tests is to verify behavior of code so that we are confident in how the code works. The
other benefit is that when you contribute to a code source that is constantly being iterated upon or added to, you want
to make sure that the changes made do not introduce any issues or change behavior. The existing tests can be re-run after
changes in code to make sure everything passes. The goal is to add new test code so that we can maintain a high test
coverage and have confidence in our code as we keep developing.

## Pytest
`pytest` is a popular testing framework that is used to write tests. pytest allows you to write a variety of tests that
can be used to test anything. The framework has many advantages ranging from being easy to use and integrate, run specific
sets of tests, skip tests, and even running tests in parallel (run multiple tests at the same time instead of doing it
serially, one by one). To use pytest, you will need to download the library using the pip tool.

```bash
pip install pytest
```

### Pytest Basics
For pytest to determine what is a test, we have to wrap test code in methods and the methods need to start with the
prefix `test`.

```python
def test_something():
    pass
```

When using Pytest, we use the `assert` keyword to validate specific scenarios. We usually try to assert a boolean value.
For example: 
```python
def test_something()
    assert 1 == 1           # This will pass and move on
    assert 0 == 1           # This will fail and throw an AssertionError
```

With Pytest, we can also validate that specific errors are thrown without breaking our tests

```python
def test_divide_by_zero_error():
    with pytest.raises(ZeroDivisionError):
        5 / 0
``` 

With really big test suites, you may sometimes need to skip a test, you can do it via the following:
```python
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    # some code that doesn't pass the test or we cannot test
```

You can also skip tests based on a condition if you would like:
```python
@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_function():
    ...
```

For more documentation on pytest, check out their [documentation](https://docs.pytest.org/en/latest/)!

## Unit Testing
Unit tests are the smallest form of tests in which individual components are tested. The goal of a unit test should be
to be concise and test a very specific function or piece of code. It is typically discouraged to write unit tests (or
even tests in general) that test more than one thing in a test. Unit tests are meant to be very quick so that you can
see the results of the tests soon after making code changes.     


### Coverage (with pytest-cov)
Test coverage is a a metric used to determine what lines of code has been covered, this helps with determining what areas
of code has been covered by tests. This gives some confidence in the code being written. Both `coverage` and `pytest-cov`
libraries are very popular when it comes to calculating the code coverage. Since we are using pytest, we can take a look
at how `pytest-cov` works. Refer to the documentation for [coverage](https://pypi.org/project/coverage/)

To install `pytest-cov`, you can use the following command
```bash
pip install pytest-cov
```

For an example, refer to the [testing-example](testing-example) directory. Here we have two different directories,
`src` and `tests`. `src` contains the functional code that we wrote and `tests` contains the tests against the code in
`src`. There is also a requirements file in there which you can download from. After taking a look at the existing code
and tests, we can take a look at how to run the tests and also see test coverage.

Installing Pytest & Pytest-Cov Requirements:
```bash
cd testing-example
pip install -r requirements.txt
```

Running Tests:
```bash
python -m pytest tests
```

Running Tests And Get Coverage:
```bash
python -m pytest tests --cov=src
```

For a more thorough walkthrough of how the test code and coverage works, check out the video!


### Mocking


## Functional / Integration Testing
\
\
\
\
[Up Next: Lesson 6 - Object Oriented Programming](../lesson06-object-oriented-programming/README.md)
\
\
\
[Go Back: Lessons 3 - Functions](../lesson03-functions/README.md)
