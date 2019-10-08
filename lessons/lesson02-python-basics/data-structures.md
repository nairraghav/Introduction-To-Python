# Data Structures
A data structure is a way of organizing data so that it can be used effectively. As we covered various data types in
the last module, we want to have a good way to organize this data so that we can use them in a programmatic and
efficient manner. 

## List
As the name suggests, a `list` is a data structure which can contain various data types. Its purpose is to contain
multiple data objects at the same time. It is an ordered data structure, meaning that whatever order items are added to
the list will stay in that order unless modified. Each element in the `list` is associated with an index, which specifies
where in the list it stays. In Python (and many other programming languages), indexing starts at 0. This means that
the first item in the list is at the 0th index. Thus, the size of a `list` is the last item's index + 1. Let's take a
look at how we can initialize a `list`!

```python
x = [1, 2, 3]               # this is a list of 3 items where 1 is the 1st item, 2 is the 2nd item, 3 is the 3rd
```

We can get a specific item from a `list` by it's index by using the square brackets after the list variable's name

```python
x = [1, 2, 3]

x[0]                        # This will return 1 since 1 is in the 0th index of the list
```

Python also allows us the flexibility of having various data types in the same `list`

```python
x = [1, "this is a string", False]

x[0]                        # 1 

x[1]                        # "this is a string

x[2]                        # False

x[3]                        # Error: You cannot access an index that has not been set
```

Once items are initialized in a `list`, we can re-write or even delete them

```python
x = [1, 2, 3]

x[2] = 5                    # x = [1, 2, 5]

del x[2]                    # x = [1, 2]

x[2]                        # Error: Cannot access this index since it doesn't exist
```

## Tuple
A `tuple` is very similar to a list except that it is immutable. Immutable means that it cannot be changed. Once a `tuple`
has its items set, we are not able to modify them by index. Tuples are also very similar to lists when it comes to
creating them. Let's take a look at how we can create a `tuple`!

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
A `set` is very similar to a list except that it cannot contain any duplicate items. It is also unordered so that when
adding a new element, there is no index that it retains which the user controls. These several features (or lack thereof)
are usually the only reasons why  someone would use a set over a list. We'll go over how to create a set and add to it:

```python
x = set()                   # create the set

x.add(1)                    # {1}
x.add(2)                    # {2}
x.add("three")              # {1, 2, "three"}
x.add(2)                    # {1, 2, "three"}  2 is not re-added since elements in a set must be unique
``` 

## Dictionary
A `dictionary` is a data structure that is based on a key/value pair. For each element in a dictionary, there is a key
and value associated with it. There are no strict requirements on what types the key/values must be, just that keys should
be unique (value do not need to be). Dictionaries are very useful and perform well when looking for items in a data structure
since you can look it up by the key value rather than an abstract index value. 

```python
x = {0: True}               # Create the dictionary

x['a'] = 'b'                # {0: True, 'a': 'b'}

x[0]                        # True

x.get('a')                  # 'b'

```


In all of the examples above, I have shown the elements within a data structure to be one of the types previously shown.
We can go a step further and use data structures as elements within other data structures. What this means is that we can
collect multiples lists within a dictionary (or any other permutation of data structures).

```python

person = {'name': "King Arthur", 'enemies_defeated': ['Black Knight', 'Troll'],
          'knows_airspeed_velocity_of_an_unladen_swallow': True}
```

\
\
\
\
[Up Next: Lesson 2 - Logic](logic.md)
\
\
\
[Go Back: Lessons 2 - Python Basics](README.md)
