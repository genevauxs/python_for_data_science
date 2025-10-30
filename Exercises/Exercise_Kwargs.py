#%% Exercise arbitrary key word arguments (**kwargs)
'''
Write a function that accepts an arbitrary number of keyword arguments.
The function should number each keyword-value pair and print it in the following format:
1: keyword -> value
2: keyword -> value
...
n: keyword -> value

a) Test what happens if you pass key word arguments in the format your_function(a=2, b=4)
This works without a problem
b) Test what happens if you pass a positional argument
It doesn't word, since no value-key pair was given
c) Test what happens if you pass key word arguments as a dictionary {"a":2, "b": 4}
Since the dictionary is seen as a value without a key, it doesn't work
d) Use the unpack-operator (**) in the call of the function to pass the keyword arguments formatted as a dictionary
After unpacking the dictionary, the key-value pairs can be accessed and printed

Start with the template given below:
'''

def print_numbered_kwargs(**kwargs):
    for ind, (key, value) in enumerate(kwargs.items()):
        print(f"{ind}: {key} -> {value}")


print_numbered_kwargs(**{"a": 1, "b": 2})
