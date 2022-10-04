"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    counter = 0
    string = ""
    for item in items:
        string = str(item)
        items[counter] = string
        counter += 1
    for item in items:
        frequencies[item] = items.count(item)
    return frequencies
