# Mocking
When thinking about writing unit tests, we have specified that they should be concise and only test a very specific
function. You may wonder, what about functions that call other functions? How do we test those? It comes down to what
you are looking to test. If you want to fully test that all the functionality works, you will want to write some
functional / integration tests below. We can also write unit tests but we use something called a `mock`. Mocks give us
a way to test functions without having to test any other functions that may lay underneath. 


## Patch
In Python, we can mock functions. We are also given the power to return back certain data if te function is called. For
example, we can create a mock for an existing function`get_number()` which can always return us the same number for
testing. Let's look at how this could work:

functions_to_test.py 
```python
# this will contain two functions that we want to test

import random

def get_number():
    return random.randint(0, 100)

def is_number_bigger_than_50():
    number = get_number()
    return number > 50
```

We can see that we cannot immediately test the `is_number_bigger_than_50` function because it also calls the `get_number`
function. What we can do is mock out `get_number` so that it always returns some number and we can check the logic works
in `is_number_bigger_than_50`. 

```python
from mock import patch

import functions_to_test

# simple unit test
def test_get_number():
    number = functions_to_test.get_number()
    # we know number has to be an integer
    assert type(number) == int
    # the randint function will return a number between 0 and 100 inclusive
    assert number >= 0 
    assert number <= 100   

@patch('functions_to_test.get_number', return_value=5)
def test_is_number_bigger_than_50_returns_false(mock_get_number):
    returned_boolean = functions_to_test.is_number_bigger_than_50()
    # check that we called the support function once
    mock_get_number.assert_called_once()
    
    # since our returned value is 5, expect false
    assert not returned_boolean
    
@patch('functions_to_test.get_number')
def test_is_number_bigger_than_50_returns_true(mock_get_number):
    # we can also specify the return value right before
    # this is handy if we plan to call it multiple times
    mock_get_number.return_value = 80
    
    returned_boolean = functions_to_test.is_number_bigger_than_50()
    # check that we called the support function once
    mock_get_number.assert_called_once()
    
    # since our returned value is 80, expect 
    assert returned_boolean
```

In the example above, we specify the use of a `patch` which is used to mock out functions and we can even give a return
value. In our example, we were mocking the `get_number` function and made it return a value of 5. From a testing perspective,
we can now validate that the `get_number` function was called by `is_number_bigger_than_50` and that it returns `False`
since the returned value is 5 (not > 50). In our third test, we noted that we don't need to specify the return value
outside of the function but we can do it inside too! We are also able to mock multiple things at once. If your function
being tested calls multiple inner functions, we can mock them all!

```python
import module

@patch('module.method_one', return_value=False)
@patch('module.method_two', return_value=500)
@patch('module.method_three', return_value='thisisastring')
def test_module_method_four(mock_one, mock_two, mock_three):
    # assume method_four calls all three methods above
    result = module.method_four()
    mock_one.assert_called_once()
    # assume the result of method_one feeds into method_two
    mock_two.assert_called_with(False)
    mock_three.assert_called_once()
    assert result == something_expected
```


## MagicMock
Outside of mocking functions, we can also mock out objects! For example, if we wanted to test something that interacts
with a JSON, we can mock out a JSON without having to create one. This is done using `MagicMock`

```python
from mock import MagicMock

def test_json_handling():
    json_object = MagicMock()
    json_object
```

\
\
\
\
[Up Next: Lesson 5 - Integration Testing](integration-testing.md)
\
\
\
[Go Back: Lessons 5 - Testing](README.md)