# Ask Ron
This is a very simple library that has been created to demonstrate how to build a Python package and deploy to PyPi such
that the code is available to anyone using the `pip` tool

## Usage
This tool can be used in two ways, you can either import it as a Python package to use in your own code or you can use
it via the Command Line to replicate a Magic 8 Ball

### Installation
You can install this Python package via the `pip` tool

```bash
pip install ask_ron
```

### Python Library


```python
from ask_ron.ask import Ask

# using the default set of answers
ask_ronald = Ask()
ask_ronald.get_answer() # this would return one of the default answers


# using a custom set of answers
custom_answers = ("Yes", "No", "I Don't Know")
ask_me = Ask(answers=custom_answers)
ask_me.get_answer() # returns one of the custom answers (randomly)
```

### Command Line
```bash
(venv) r.nair@Mac ask_ron $ ask_ron
What is your question? Will I become famous?
Outlook not so good.
```

## Release Manager
- Raghav Nair (@nairraghav)