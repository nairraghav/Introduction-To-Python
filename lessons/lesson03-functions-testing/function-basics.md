# Function Basics
A function is a named chunk of code that performs some specific task. Functions are used to typically run the same piece
of code without having to rewrite the same bits over and over again. Functions can take in some input and return output
but neither are specifically required. Functions are generally used to help write neat and optimal code and comprise one 
of the big building blocks that make up programming. The syntax for specifying a block of code to be a function is to use
the `def` keyword followed by the name of the function and a colon, the block of code should be indented one level after.
The naming standard to follow with functions is that they should be lower case using underscores as necessary. 

Example:
```python
def hello_world():
    print('Hello World!')

def hello(name):
    print('Hello ' + name)              

hello_world()                       # Prints 'Hello World!'
hello("Ron")                        # Prints 'Hello Ron'
hello("Sally")                      # Prints 'Hello Sally'
```

## Docstring
Docstrings are a way to document code. It is simple a multiline string that describes the intended goal of a function
so that someone who has not written the code can easily/quickly understand what the code is doing and how they could
go about using it. We use triple quotes to signify a multiline string. The docstring is the first line(s) following the
declaration of the function. Some IDEs have the benefit of showing the user a docstring when you hover over a function.

Example:
```python
def hello(name):
    """This function prints out "Hello" followed the name specified as the parameter
    :param name: A string which represents the name printed after "Hello"""
    print ("Hello", name)
```

In the example below, when calling the StormCastle function, PyCharm shows the docstring displaying what the parameters
are and their descriptions. There are more settings that you can set within the IDE in terms of what format to follow
for doc strings. Typically, it is good behavior to describe what the function does (if it's non-obvious), what parameters
it requires, and what it returns (covered below!)
![pycharm-example](https://i.stack.imgur.com/0Kc6e.png)

## Parameters
Parameters are the variables that are accepted by functions in the parenthesis of the declaration. Some functions may
take zero parameters, some may take many! In general, you should avoid requiring too many variables in the function
declaration as it can get crowded and be visually hard to follow. We will cover using args/kwargs as a method of getting
by this!

### Optional
One neat thing we can do with parameters is make them optional so that the user does not need to specify them unless they
know that they need a non default value. 

Example:
```python
def print_name_multiple(name, times=1):
    print(name*times)

print_name_multiple('ron')                      # Prints 'ron'         
print_name_multiple('ron', 5)                   # Prints 'ronronronronron'
```

The only requirement when using optional parameters is that the MUST be the last parameters in the function declaration.
Otherwise, there is no way for the Python interpreter to know what parameters are being passed into the function. 

### args
`*args` is an easy way to specify that a function can take many more parameters without specifying their names. Specifying
the asterisk before args unpacks the values of all the parameters into a tuple called args. This allows us to pass in 
many parameters when calling the function without specifying them all in the function declaration. Let's take a look at
how we can create a sum function with this.

We don't want to follow this method below because if we ever want to add another parameter to add, we need to specify it
```python
def sum_two(a, b):
    print (a + b)

def sum_three(a, b, c):
    print (a + b + c)


sum_two(1, 2)    
sum_three(1, 2, 3)
```

Instead, we can use args to pass in as many as we want
```python
def print_sum(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


print_sum(1, 2)
print_sum(1, 2, 5, 10)
print_sum(1, 2, 5, 10, 50, 100)
```

### kwargs


### argparse


### Environment Variables


## Return


## \_\_main__


## Recursion

\
\
\
\
[Up Next: Lesson 3 - Pytest](pytest.md)
\
\
\
[Go Back: Lessons 3 - Function Basics](README.md)
