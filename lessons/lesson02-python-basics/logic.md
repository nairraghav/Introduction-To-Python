# Logic
The basics of any program (python or not) is some basic logic that can be applied and worked upon to create simple to
advanced programs. We will take a look at some of the basic logic flows.
    
## If Statement
An `if` statement evaluates an expression to `True` or `False`. If the result of the expression is `True`, we do
something. We can also make it do something in the `False` scenario.

```python
x = 5

if x == 5:
    print("x is 5")                 # Prints x is 5
else:
    print("x is not 5")             # This will not print
``` 

```python
x = 5

if x == 0:
    print("x is 0")                 # This will not print
else:
    print("x is not 0")             # Prints x is not 0
``` 

We can also have multiple branches within an `if` statement multiple cases.

```python
x = 5

if x == 0:
    print ("x is 0")                # This will not print
elif x == 5:
    print("x is 5")                 # Prints x is 5
else:
    print("x is a mystery")         # This will not print
```

Within these logical statements, Python gives us some built-in tools to help give us the ability to specify our scenarios.
Within this, we will cover `is`, `not`, `and`, `or`.

### is
The keyword `is` is used, similiarly to `==`, to compare identity. `==` is used to evaluate the value meanwhile `is`
evaluates if the objects being compared are the same or not. Let's take a look at how this works!

```python
a = [1, 2, 3]
b = a

a == b                              # This returns True because both a and b have the same value [1, 2, 3]

a is b                              # This also returns True because b points to the list a

b = [1, 2, 3]

a == b                              # Again, this returns True because both a and b have the same value [1, 2, 3]

a is b                              # Now, this returns False because while b now points to a new list with the same value 
```

### not
As you would think, the `not` keyword negates the value of the expression it precedes.

```python
a = 1

b = 2

c = a

c is a                              # This returns True since c and a point to the same int

c is not b                          # This returns True since c and b point to different ints

c is not a                          # This returns False since c and a point to the same int
```

### and
`and` is a keyword is used to conjoin to expressions and return a value for their joint result. The result will only
return `True` if the expressions being conjoined by the `and` are all `True` as well. If any of those individual
expressions return `False`, the `and` instantly results in `False`. As a note, we can use parenthesis to more easily
read our expressions.

```python
a = 1

b = 2

if (a == 1) and (b == 2):
    print("True")                   # This will be printed
    
if (a == 0) and (b == 2):
    print("True")                   # This will not print
elif (a == 0) and (b == 1):
    print("True")                   # This will not print        
else:
    print("False")                  # This will be printed
```

### or
`or` is very similar to `and` except that we only need one of the expressions to return `True` for the entire expression
to return `True`.

```python
a = 1

b = 2

if (a == 1) or (b == 2):
    print("True")                   # This will be printed
    
if (a == 1) or (b == 0):
    print("True")                   # This will be printed
    
if (a == 0) or (b == 2):
    print("True")                   # This will be printed
```

## For Loop
A `for` loop is a programmatic way of repeating some set of actions for a given number of times. The goal of a for loop
is to avoid writing redundant code over and over if it will be repeating the same actions.


```python
fruits = ["apricot", "blueberry", "cantaloupe"]

# If I wanted to print each item in the list, I might want to print it by the index
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Another way to do this would be using a for loop and the range function
# Don't worry about functions for now, just know that range(3) gives you a list of numbers starting from 0 to the
# number passed in (exclusive). So 0, 1, and 2
for x in range(3):                  # x will represent the values from the range function
    print(fruits[x])                # This will print apricot, blueberry, and cataloupe each in new lines

# Python also gives us a very easy way to use for loops with data structures
for fruit in fruits:                # We will iterate through the fruits object and fruit will represent that value
    print(fruit)                    # This has the same functionality as above
```

As you can see, using `for` loops is very useful in writing neater and more readable code while giving the same
functionality.


## While Loop
A `while` loop is just like a for loop except instead of giving a set amount of iterations to go through, it will enter
the loop while a given expression expression is `True`. The iterations will continue until repeating the block of logic
until the expression returns `False`. When using while loops, you need to be very careful because if that expression
never resolves to end, the code will continue to run infinitely. The process will never end until you close/terminate
the program.

```python
x = 0

while x < 5:
    x += 1                          # This will increment the value of x each time until (x < 5) no longer returns True

print(x)                            # This will print 5 since that is when x < 5 is no longer True
```

In terms of pure functionality, you will generally be able to substitute `for` loops with `while` loops and vice versa.
The key is understand when to use each which type of loop and what allows for it to be the most understandable.
Generally, `for` loops are preferred for iterative needs because you will usually know how many times an iteration must
be done, they are much more readable and there is typically less risk when it comes to having infinitely running loops
as there is usually a well defined end.
\
\
\
\
[Up Next: Lesson 3 - Functions & Testing](../lesson03-functions-testing/README.md)
\
\
\
[Go Back: Lessons 2 - Python Basics](README.md)
