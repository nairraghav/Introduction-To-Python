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
\
\
\
\
[Up Next: Lesson 1 - Python Interpreter](python-interpreter.md)
\
\
\
[Go Back: Lesson 1 - Environment Setup](README.md)
