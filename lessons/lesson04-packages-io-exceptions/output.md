# Output
As we've seen in the past with our examples, as well as being able to take in text and data, we can also print it back
out. Similar to input, we can print out directly to the console or wherever the code is running or we can write to a
file. There are reasons and benefits to both and it will be up to you to determine what fits your needs better

## Console
As we've seen many time, we can print things to the console via the print command

```python
print('hello')                              # basic print

x = 5
print('This is a number: {}'.format(x))     # print with formatting


print(f'the number {x} is five')            # print using f-string
``` 

One thing we haven't introduced as some escaped characters we can put in strings to create tabs, new lines, and other
little helpers.

```python
# this will print two separate lines
print('this is a line\nthis is on another line') 

# this has print two strings with a tab between them
print('this is a string\tthis string has been tabbed over')

# use the backslash before the quote to let python know
# that we want to print a quote, not end the string
print('this is how you print a quote: \'')         

```

## Writing Text Files
Writing to files, in general, is very similar to how we read from them. We first need to open the file in the correct
permissions view and then we can proceed on!

```python

with open('output.txt', 'w') as write_txt_file:
    write_txt_file.write('This is the first line\n') # if you don't use \n you will have everything on one line
    write_txt_file.write('Here is a second line\n')
```

## Writing CSV Files
```python
import csv

with open('output.csv', 'w') as write_csv_file:
    csv_writer = csv.writer(write_csv_file, delimiter=',')
    for i in range(5):
        csv_writer.writerow([i, f'This line is #{i}']) # each item in the list makes up the delimited line
```

Unlike the text file, you do not need to specify the new line. The csv_writer will end the line after it has printed
everything in the row.

## Writing JSON Files
Writing JSON to a file is 

```python
import json

# since JSON is really just a dictionary, we can print out a dictionary to a json file
# we can also take in an input json file, modify it, and push it back out
output_json = {"sample": {"first": True, "fake": True, "data": ["a", "b", "c"]}}

with open('output.json', 'w') as output_file:
    json.dump(output_json, output_file)
```

Just like how there is a `json.loads`, there is also a `json.dumps` function which will take some dictionary/JSON and
output it as a string.

Also, as mentioned with inputs, we can use the argparse library to take in the output file name when calling the program so we
can create new files with a dynamic name rather than a hardcoded static one.

\
\
\
\
[Up Next: Lesson 4 - Logging](logging.md)
\
\
\
[Go Back: Lessons 4 - Packages, Input/Output, & Exceptions](README.md)