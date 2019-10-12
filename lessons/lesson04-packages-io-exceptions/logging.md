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
A `StreamHandler`, as the name suggests, will be outputting the logs directly to some stream which can support a `write()`
and `flush()` operation. For now, you can think of the StreamHandler as what is user to print to the console. The benefit
of using a StreamHandler is that you can directly see the output as the program is running. The problem may occur that
there are too many logs flying by to immediately recognize anything. People use formatting and colors to quickly distinguish
how the programming is running. For example, any red text may indicate a failure.


### FileHandler
Working very much similar to a StreamHandler, a `FileHandler` writes to a specified file. Anytime the log function is
called with a string, we log that string in a file (which can be viewed or parsed at some time).


## Logging Levels
As previously mentioned, the benefit of logging vs printing directly is that we can set levels to our handlers so that
we don't end up blasting everything at the user. We may choose to only throw specific critical failure messages to the
`StreamHandler` so that we can quickly tell if there are any failures and log everything using the `FileHandler` so that
we can revisit the log later if needed. When it comes to logging levels, refer to the follow ordered list of importance,
starting with the least important.

1. Debug
2. Info
3. Warn
4. Error
5. Critical

When specifying a level for your log, everything that is prioritized above your level will also be printed. What this
means is that if you set the `WARN` level, you will also get `ERROR` and `CRITICAL` since they are even more higher
priority than the other levels. Typically, this makes sense because if you want warnings of a lower level, you will
definitely want higher level failures as well.


## Logging Example
Let's take a look at a logger example below:

```python
import logging

# create our logger
logger = logging.getLogger('logger')
# we need to set this here because the default will set to WARN
logger.setLevel(logging.DEBUG)

# create our handlers that we want to use with logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler = logging.FileHandler("log_file_name.log")
file_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

print(logger.getEffectiveLevel())

# this will show up on both
logger.critical("This is a critical message")

# this will only show on the file
logger.debug("This is a debug message")
``` 

As noted in the code above, when creating a logger, the default is set to `WARN`. So even though our `FileHandler` wants
to go as low level as a debug, it will never get there because the logger itself doesn't capture anything below a `WARN`
to pass on to its handlers. Your logger level will determine what is passed down to the handlers, which can have their
own levels.
 
\
\
\
\
[Up Next: Lesson 4 - Exceptions](exceptions.md)
\
\
\
[Go Back: Lessons 4 - Packages, Input/Output, & Exceptions](README.md)