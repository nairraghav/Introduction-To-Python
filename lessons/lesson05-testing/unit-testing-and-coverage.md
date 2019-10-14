# Unit Testing
Unit tests are the smallest form of tests in which individual components are tested. The goal of a unit test should be
to be concise and test a very specific function or piece of code. It is typically discouraged to write unit tests (or
even tests in general) that test more than one thing in a test. Unit tests are meant to be very quick so that you can
see the results of the tests soon after making code changes.     


## Coverage (with pytest-cov)
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

\
\
\
\
[Up Next: Lesson 5 - Mocking](mocking.md)
\
\
\
[Go Back: Lessons 5 - Testing](README.md)