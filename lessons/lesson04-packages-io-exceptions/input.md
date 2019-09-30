# Input
Python can also be used to take input of varying types, ranging from user input on the command line to reading entire
files. In this section, we'll go over some common examples but there is a LOT more in depth that you can go that will
not be covered. Please check out the [Python documentation](https://docs.python.org/3/tutorial/inputoutput.html) if 
you want even more detail. 

## User Input
One example of input that can be provided is when a user provides information to a program. This is done using the
input function. When the input function is used, the data that is passed back is read as a string so you will need
to convert it to a different type if you are not looking to work with a string.

String Example
```python
# This will print "What is your name? " and wait for the user to give an input
name = input("What is your name? ")
print(f"Hi {name}")     # Here we also introduce f-strings (available in Python 3.6+)
                        # You can define an f-string by putting an 'f' before the quotation marks
                        # Using f-strings allow you to efficiently put variables within strings
                        # This is neater than using "Hi " + name or "Hi {}".format(name)
```
![string-example](../assets/lesson4-name-example.png)


Integer Example
```python
age = int(input("How old are you? "))   # Note we add a space after the question to the command line is neater
                                        # We also wrap everything inside int() to convert the answer to an integer
print(f"Wow, you're {age} years old!")
```
![integer-example](../assets/lesson4-age-example.png)

## Reading From Files


### Text


### CSV


### JSON


## Input Arguments


### argparse


\
\
\
\
[Up Next: Lesson 4 - output](output.md)
\
\
\
[Go Back: Lessons 4 - Packages, Input/Output, & Exceptions](README.md)