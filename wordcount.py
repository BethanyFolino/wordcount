#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = """Bethany Folino and
https://www.kite.com/python/answers/how-to-count-item-frequency-in-python
https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given
-text-file-using-dictionary/
https://www.discoverbits.in/1562/attributeerror-dict-object-attribute-most_
common-python"""

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    import collections
    frequency = {}
    with open(filename) as text:
        for word in text.read().split():
            if word.lower() in frequency:
                frequency[word.lower()] += 1
            else:
                frequency[word.lower()] = 1

        new_dict = collections.OrderedDict(sorted(frequency.items()))
        return (dict(new_dict))


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    import collections
    frequency = {}
    with open(filename) as text:
        for word in text.read().split():
            if word.lower() in frequency:
                frequency[word.lower()] += 1
            else:
                frequency[word.lower()] = 1

        new_dict = collections.OrderedDict(sorted(frequency.items()))
        for key in list(new_dict.keys()):
            print(key, ":", new_dict[key])


def print_top(filename):
    """Prints the top count listing for the given file."""
    import collections
    frequency = {}
    with open(filename) as text:
        for word in text.read().split():
            if word.lower() in frequency:
                frequency[word.lower()] += 1
            else:
                frequency[word.lower()] = 1

        new_dict = collections.OrderedDict(sorted(frequency.items()))
        counted = collections.Counter(new_dict).most_common(20)
        top_twenty = dict(counted)
        for key in list(top_twenty.keys()):
            print(key, ":", top_twenty[key])


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
