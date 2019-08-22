# What is Python?
Python is a high-level programming language that uses an object oriented approach to help create clean, readable, logical
code for small and large applications/projects. One of the main goals for Python is to be an easily readable language.
Heavily relying on the usage of whitespace and not requiring the common curly braces or semicolons allows the code to 
be uncluttered and easily read. 

# Python3
There are currently two major versions of Python that are used in the industry: Python2 and Python3. While some still 
use Python2, it should be considered as legacy code while Python3 should be what everyone is using. Python2.7 is the
final major release of Python2.x and the end of life has been [confirmed](https://pythonclock.org/). 

# Installing Python

## Windows
![you-chose-poorly](https://i.pinimg.com/originals/5a/42/97/5a4297bac22f1fa0ef13d5ec1d67b366.jpg)


## Mac
Lucky for you, Mac OSX (10.8+) has Python installed (yay!) but it is Python2 (womp womp). To download/install Python3,
refer to the this helpful [document](https://docs.python-guide.org/starting/install3/osx/). I have listed the steps below
for convenience:
* Open a Terminal
    * Open Spotlight (command + space)
    * Type in Terminal and hit Enter
* Install Homebrew
    * ```bash
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
      ```
    * Depending on your OS Version:
        * OS X (10.13+)
            * ```bash
                export PATH="/usr/local/opt/python/libexec/bin:$PATH"
              ```
        * OS X (10.12 or lower)
            * ```bash
                export PATH=/usr/local/bin:/usr/local/sbin:$PATH
              ```
* Install python
    * ```bash
        brew install python
      ```
* Check Python Version
    * ```bash
        python --version
      ```
        * If you don't see anything here, check if the following works
        ```bash
            python3 --version
        ```


# Text Editor / IDE
To start writing Python code, you will need a text editor at the very least. You can even start writing in Notepad. For
coding purposes, programs like [Notepad++](https://notepad-plus-plus.org/), [Sublime](https://www.sublimetext.com/), and 
[Visual Studio Code](https://code.visualstudio.com/) are very popular for tasks like this. If you are planning to code a
lot in Python, I would recommend getting [PyCharm](https://www.jetbrains.com/pycharm/) (there is a free community edition).
Using an IDE (Integrated Development Environment) can provide to be more beneficial as the program will have shortcuts,
visual cues, and suggestions to help improve productivity. While this can be beneficial, it is by no means a requirement.
Certain text editors like the ones mentioned above can download plugins which can help in similar ways.


# pip
pip is the package management system used by Python to download/install software packages written in Python. While many
packages come with the default installation of Python, you will find that you need to install certain packages through
the use of pip. pip should come installed with Python and is very easy to use in the command line. 

```bash
    pip install \<package-name\>
```

```bash
pip uninstall \<package-name\>
```


# Virtual Environment
Virtual Environment is a tool that is used to isolate python programming environments to avoid having collisions when it
comes to programmatic requirements. It is usually a good idea to have a separate virtual environment per project.

## Installation
Virtual Environment can be installed through pip:
```bash
pip install virtualenv
```

## How To Use

### Creating Virtual Environment
```bash
virtualenv venv
```

You can call `venv` any name but that is a common one.

### Activating Virtual Environment
This will create a virtual environment that mirrors the setup on your machine inside a directory called venv. To activate
this, you will want to run:
```bash
source venv/bin/activate
```

You can see that the virtual environment is active because the name of the Virtual Environment (venv) will be shown at
the beginning of the line in the console
```bash
Raghavs-MBP:Introduction-To-Python rnair$ source venv/bin/activate
(venv) Raghavs-MBP:Introduction-To-Python rnair$
```

### Deactivating Virtual Environment
To deactivate the virtual environment, you can just type:
```bash
deactivate
```

[Go Back To Lessons](../../lessons#python-lessons)