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
\
\
\
\
[Up Next Lesson: Text Editors / IDE](text-editor.md)
\
\
\
[Go Back: Lesson 1 - Environment Setup](README.md)
