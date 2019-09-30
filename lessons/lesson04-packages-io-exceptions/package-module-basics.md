# Modules and Packages
Within python, we can use existing Python code to our benefit. You never want to re-invent the wheel. Why waste time
building a tool when there could already be an existing solution that may do what you want AND more? As mentioned previously
in the pip section, we are able to download existing libraries of code. We will investigate certain libraries that will
be helpful. Beyond using other people's code, we sometimes create multiple files within a directory for python code to
differentiate the purpose of files. For example, you may have a `hello.py` file which handles some functions to say hello.
Similarly, you may have another file, `get_info.py`, which does other things like asking for the user to input a name and pass that
name to other functions! In this section, let's take a closer look on how we can use libraries that others have written 
and what we have created ourselves.

## Modules
A module is a single python file that can be imported. For example, when we want to use `get_info.py` methods within our
`hello.py` file, you want to import that module. The import section below will show how we can do that!

## Packages
A package is a directory of modules. A package gives us the opportunity to keep code organized. Packages come in handy 
so we can keep modules in one area. For example, we may have a package called `user` which has the modules `get`,
`create`, `delete`. 

### \_\_init__.py
To create a Python package, you must have a file within the directory (and all subdirectories of said package) called
`__init__.py`. This file just has to exist, we don't need to put any information within it, nice and easy!

## Imports
First and foremost, after a specific file is written, you will need to start the file you want to use that behavior in
with some imports. The `import` keyword is used to pull in modules and packages. If we have the file in the same directory,
you can import it like the following:

### Import Module 
```python
import get_info # notice that you drop the .py

# we can now use the get_info module to call methods that may exist
name = get_info.ask_for_name()
```

### Import Package
```python
import user # importing our whole user module
from user import create # here within our user package, we are importing create

created_user = create.create_user()
found_user = user.get.get_user(created_user.id)
```
Typically, it is good behavior to only import modules that we are going to use. We do not want to import entire packages
if we are not going to use them. This helps keep things neat and tidy.

### Import Aliases
Sometimes, we may deal with packages that are not named optimally or are just too long. To remedy this, during the import,
we can modify the name of said package or import.

```python
import this_is_too_long as long
from super_package import smaller_package as sm_pack

long.do_something()
sm_pack.do_something_else()
```

## Setting Up Imports
When importing files locally, you may run into import issues depending on where you run the code from. Typically, you want
to organize your code such that you can run everything from a root directory. This means that all your imports should be
relative to that root directory. Take a look at our [testing example](../lesson05-testing/testing-example) to see how
this is done! Things are organized so that you run everything within the `testing-example` directory, look at the imports
within the files in src and the test directories.

\
\
\
\
[Up Next: Lesson 4 - Input](input.md)
\
\
\
[Go Back: Lessons 4 - Packages, Input/Output, & Exceptions](README.md)