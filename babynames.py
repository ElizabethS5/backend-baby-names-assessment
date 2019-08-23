#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

__author__ = "ElizabethS5"

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    text = get_text(filename)
    year = re.search(r'Popularity\sin\s(\d{4})', text).group(1)
    rank_names_tups = re.findall(
        r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    names_dict = create_names_dict(rank_names_tups)
    names_list = sorted([tup[0] + ' ' + tup[1]
                         for tup in names_dict.items()])
    names_list.insert(0, year)
    return names_list


def get_text(filename):
    with open(filename, 'r') as f:
        return f.read()


def create_names_dict(tuples):
    names_dict = {}
    for tup in tuples:
        if tup[1] not in names_dict:
            names_dict[tup[1]] = tup[0]
        if tup[2] not in names_dict:
            names_dict[tup[2]] = tup[0]
    return names_dict


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def create_summary_file(file, text):
    file_name = file + '.summary'
    with open(file_name, 'w') as f:
        f.write(text)


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    # option flag
    create_summary = args.summaryfile

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    for file in file_list:
        text = '\n'.join(extract_names(file)) + '\n'
        if create_summary:
            create_summary_file(file, text)
        else:
            print(text)
    # or write it to a summary file


if __name__ == '__main__':
    main()
