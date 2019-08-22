# Variables
A variable is a container for storing data values. We can set a variable equal to some text, a
number, and several other things. In programming, variables are handy tools which we use all
the time. Let's take a look at how to use them!

```python
x = 5
```
In this example, we set the variable (named x) equal to the number 5. After this line, the
variable x will always have the value 5, until it is either changed or deleted.

```python
x = 5       # x = 5

x = x + 5   # x = 10

x = x * 2   # x = 20
```

Python also allows us to change the TYPE of data being represented by a variable (which most
other programming languages will not allow). 
```python
x = 5       # x is what we can all "integer" representing a number

x = "hello" # x is now a "string" which represents some text
```

One thing we can do with variables is to check if they are equal in value to other things. We
do this with `==` or the keyword `is`.
```python
x = 5

x == 5      # True

x == 2      # False

x == "5"    # False
```

Lastly, we can delete variables if we know we no longer need them. This can be done to conserve
space so that we don't have a million variables, if we're not using them. To delete variables
(and typically anything else), we use the `del` keyword.

```python
x = 5       # x = 5

del(x)

x           # Error: x doesn't exist anymore
```
\
\
\
\
[Up Next: Lesson 2 - Types](types.md)
\
\
\
[Go Back: Lessons 2 - Python Basics](../README.md)
