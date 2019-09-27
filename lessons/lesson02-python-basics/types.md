# Types
As seen in the previous topic, there are types in Python. We initially looked at an `int` and
a `string`. We will discuss those and a couple others below.


## Boolean
A `boolean` is essentially a binary value (meaning it has 2 potential values). Typically, booleans
are used to represent `True` or `False`. Booleans are usually used in evaluating some sort of
logic, such as checking if variables are equal to each other.

```python
x = True            # x represents a Boolean (True)

x is True           # True, because x = True

x is False          # False, because x = True
```

Booleans can also be represented with numbers. 0 represents `False` while 1 (or any other number)
represents `True`.


## String
As seen before, a `string` represents 1 or more text characters that are wrapped with quotes. These
quotes can be single `'` or double `"`, but which ever is used to start the string, must also
end the string.

```python
x = 'this is a string'  # Valid

y = "this is a string"  # Valid

x == y                  # True (Even though they use diff quotations to start/end, they are equal)
```


## Int
An `int`, or integer, represents a whole number (positive or negative). Similar to numbers in real
life, we can run the general operations on them. 

```python
x = 5                   # x has a value of 5

x = x + 10              # x has a value of 15

x = x * 2               # x has a value of 30

x = x / 3               # x has a value of 10

x = x - 9               # x has a value of 1

# A shortcut of writing what we did above would be:
x += 3                  # equivalent to x = x + 3 (x has a value of 4)

x *= 2                  # equivalent to x = x * 2 (x has a value of 8)
```

\
\
\
\
[Up Next: Lesson 2 - Data Structures](data-structures.md)
\
\
\
[Go Back: Lessons 2 - Python Basics](README.md)
