# Errors
Errors, also known as Exceptions, are a very common part of Python which you have likely already seen. Errors are
raised when Python doesn't know how to handle something or we can throw them manually as well (usually for specific
handling of situations). Let's look at a simple mathematical example:

```python
5 / 0 # we try to divide by 0
```

```
Traceback (most recent call last):
  File "logger.py", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero
```

As you can see above, when you try to run some code which cannot be handled, an error is thrown. Luckily, there is a
readable name which tells us what the issue is `ZeroDivisionError`. Typically, the error names are well named so that you
should have an idea as to what could have gone wrong. Similarly, if you decide to create your own error, you should try
to give it an easy to understand name so the user is not left wondering what the issue is.

## Common Errors 

### AttributeError
The `AttributeError` is raised when we try to access an attribute of a variable that doesn't exist. This can happen when
```python
from datetime import datetime

today = datetime.now()  # creates a datetime object for the current date at the current time
today.date              # returns todays date
today.not_attribute     # raises AttributeError
```

### ImportError / ModuleNotFoundError
Both the `ImportError` and `ModuleNotFoundError` usually occurs when we try to import something that doesn't exist. There
are usually a couple of common reasons this can occur.
1. Typo in import
2. Package is not installed
3. \[Part of\] Package location is incorrect

```python
import jsoon                # raises ModuleNotFoundError
                            # this is because jsoon doesn't exist

from datetime import lol    # raises ImportError
                            # this is because datetime exists but lol doesn't
```

### IndexError
`IndexError` is a frequently encountered error that occurs when we try to access an index of a data structure (list,
tuple, etc) that doesn't exist. 

```python
a = [1, 2, 3]

a[0]        # returns 1

a[4]        # raises IndexError

``` 

### KeyError
The `KeyError` is the dictionary equivalent of the IndexError. This happens when we try to access a dictionary with a key
that does not exist. This can usually be resolved by using the `get` method for a dictionary.

```python
a = {"a": "a", "b": "b"}
a["a"]      # returns a
a["c"]      # raises KeyError

a.get("c")  # will not raise Error, returns None
```

### NameError
`NameError` is raised when we try to access something that has not yet been defined.
```python
a = 1

a   # returns 1
b   # raises NameError
``` 

### SyntaxError
`SyntaxError` is a frequent error that can occur when you mistype something. For example, if we mistype `while` in a loop.

```python
whille True:        # raises SyntaxError
    do_something()

```

### TypeError
A `TypeError` is raised when an operation or function is ran on a value that is the wrong type. This can happen when 
trying to get the length of a variable. This works for a string but not for an int.

```python
len("this string")  # this returns 11

len(5)              # raises TypeError (expecting string)

```

### Value Error
`ValueError` is another common error that is raised when an operation or function is run on an inappropriate value. A
common example is when you try to convert a string into an integer but the value does not make sense.

```python
a = '5'
int(a)  # returns 5

a = 'five'
int(a)  # raises ValueError
```

### ZeroDivisionError
As the name suggests, `ZeroDivisionError` occurs when we try to divide by zero as per our example above.


## Handling Errors
When errors occur, the program will end and sometimes this can be confusing to the User because they may still expect
some functionality to go through. We use a try/except block to try some piece of code and "catch" an error if it occurs.
Under the except block, we add some logic for what should happen if the error occurs. It is a good habit to specify what
error we are expecting instead of using the general `Exception`. This is because you may be expecting a `SyntaxError` but
a `ValueError` may occur but you are handling it in a different way. Let's look at an example below which also takes
advantage of logging to note the failure. 

```python
import logging

logger = logging.getLogger('numbers')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler)


string_nums = ['1', '2', '3', '$', '5', '6']
int_nums = []

for number in string_nums:
    try:
        logger.debug(f'Trying to convert {number}')
        int_nums.append(int(number))
    except ValueError:
         logger.error(f'ERROR: Failed To Convert {number}')
``` 

With the try/catch block, we can also add an `else` and a `finally` block which handles what happens in the case of a
non-error and what should be done after everything in the try block has finished.

```python
try:
    file = open('file_name.txt', 'r')
    do_something_that_may_cause_error()
except ValueError:
    handle_value_error()
except IndexError:
    handle_index_error()
else:
    no_errors_occured()  # typically is not used
finally:
    file.close()  # this will run regardless of error or not
```

The main benefit of the else block is to add code that may be in the try block that shouldn't be there. It is a good habit
to ONLY put code in the try block which will trigger the error. Anything else should be put in the else/finally.

## Raising Errors
When running your code, you may run into errors and handle them. Another thing you may want to do is to raise an error
yourself if you foresee an issue. Since you, the developer, have an idea of how the code should work. You may note specific
situations where an error can come up. For example, if you code expects a string but receives an int, you can handle throw
a TypeError early on.

```python

user_input = input("Please enter a number below 10: ")

if int(user_input) >= 10:
    raise Exception("The Int Must Be Less Than 10")
```


## Creating Your Own Exception
We will go more into creating objects at a later time but you may find yourself wanting to create an exception. This 
can be done using the following:

```python
class ValueTooLargeError(Exception):
    pass # we will use the generic Exception to handle everything

user_input = input("Please enter a number below 10: ")

if int(user_input) >= 10:
    raise ValueTooLargeError("The Int Must Be Less Than 10")
```

\
\
\
\
[Up Next: Lesson 5 - Testing](../lesson05-testing/README.md)
\
\
\
[Go Back: Lessons 4 - Packages, Input/Output, & Exceptions](README.md)