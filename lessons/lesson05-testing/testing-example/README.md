# Testing Example 
This directory is an example of how you can write unit tests and integration tests for some simple python code. In our
`src` directory, we have some basic python code which is used to do simple arithmetic operations. There are also two
test directories that are used to separate our unit and integration tests. The unit tests are quick tests which are to be
run anytime code is modified in anyway to ensure that the functionality has not broken. The integration tests are more
real examples of how the code should be used to validate typical user scenarios. In the case of our simple code, the
integration tests may look similar to unit tests.

For a better example, think about how web services work. Unit tests will test the inside nitty gritty detail code and 
the internal functions that allow the whole piece to come together while the integration tests validate the behavior of
the services that a user would see. 

To get a good understanding of how things work, please start by looking at the source code to see what it does and some
sample tests to see how we have gone about validating it. After getting a bit familiar with the code, check out the video
walk-through in this directory which will go deeper in

## Installing Example Requirements
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

For a more thorough walk-through of how the test code and coverage works, check out the video below!


# Video Walkthrough
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

\
\
\
\
[Up Next: Lesson 6 - Object Oriented Programming](../../lesson06-object-oriented-programming/index.ipynb)
\
\
\
[Go Back: Lessons 5 - Testing](../index.ipynb)