# Data Structures
A data structure is a way of organizing data so that it can be used effectively. As we covered various data types in
the last module, we want to have a good way to organize this data so that we can use them in a programmatic and
efficient manner. 

## List
As the name suggests, a `list` is a data structure which can contain various data types. It's purpose is to contain
multiple data at the same time. It is an ordered data structure, meaning that whatever order items are added to the
list will stay in that order unless modified. Each element in the list is associated with an index, which specifies
where in the list it stays. In python (and many other programming languages), indexing starts at 0. This means that
the first item in the list is at the 0th index. Thus, the size of a list is the last item's index + 1. Let's take a
look at how we can initialize a list!

```python
x = [1, 2, 3]               # this is a list of 3 items where 1 is the 1st item, 2 is the 2nd item, 3 is the 3rd
```

We can get a specific item from a list by it's index by using the square brackets after the list variable's name

```python
x = [1, 2, 3]

x[0]                        # This will return 1 since 1 is in the 0th index of the list
```

Python also allows us the flexibility of having various data types in the same list

```python
x = [1, "this is a string", False]

x[0]                        # 1 

x[1]                        # "this is a string

x[2]                        # False

x[3]                        # Error: You cannot access an index that has not been set
```

Once item's have been in a set, we can re-write or even delete them

```python
x = [1, 2, 3]

x[2] = 5                    # x = [1, 2, 5]

del x[2]                    # x = [1, 2]

x[2]                        # Error: Cannot access this index since it doesn't exist
```

## Tuple
A `tuple` is very similar to a list except that it is immutable. Immutable means that it cannot be change. Once a tuple
has it's items set, we are not able to modify them by index. Tuples are also very similar to lists when it comes to
creating them. Let's take a look at how we can create a tuple!

```python
x = (1, "tuple item", True)              

x[0]                        # 1

x[1]                        # "tuple item"

x[2]                        # True
```

As mentioned previously, these indices are immutable so we cannot update nor delete them. The only way to "modify" them
is to create a new tuple and change the value that you want. You probably don't want to do this and instead if you know
that your data structure is going to change, use a list.

## Set


## Dictionary

\
\
\
\
[Up Next: Lesson 2 - Logic](logic.md)
\
\
\
[Go Back: Lesson 2 - Types](types.md)