#!/usr/bin/env python3
"""
Learning the webbrowser module for scraping the internet.
"""

import sys, webbrowser, pyperclip

# using 'www.yourcountdown.to' for example
# webbrowser.open('https://yourcountdown.to')

"""
# Script to run google maps and search for address directly from terminal.
# Using sys.argv
"""

# Command line argument will look something like this:
# sys.argv ['name_of_file', 'str_1', 'str_2', 'str_3']
sys.argv

# Check if command arguments are passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)
sys.exit()








