# Logging
A lot of what we've been doing with printing output is to help debug issues but there is a better way to do that,
logging! Logging has some inherent benefits of use versus just outputting everything. With logs, we can control whats
being outputted, define what information we want to put, control how things look, and also setting where the logs live.
Logging allows us to set severity levels to our output so that we can filter out things that are low level logs vs
high priority critical issues. Having a slew of output is nice when we want to go back and parse logs to see where things
went wrong but it can output so much data that is hard to follow actively. Instead, we can configure it so that we only 
get warnings and errors to log to the console while everything else goes to a log file (which can be looked at for 
further detail). Let's take a look at what all we can do!

## Loggers
Within logging, there are two main types of loggers that we will be introducing: `stream` and `file`. For more information
on other types of handlers, refer to the [documentation](https://docs.python.org/3/library/logging.handlers.html)


### StreamHandler


### FileHandler


\
\
\
\
[Up Next: Lesson 4 - Exceptions](exceptions.md)
\
\
\
[Go Back: Lessons 4 - Packages, Input/Output, & Exceptions](README.md)