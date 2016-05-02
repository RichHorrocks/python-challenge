#!/usr/bin/env python

import sys
import re
import urllib
from bs4 import BeautifulSoup, Comment

page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
soup = BeautifulSoup(page.read(), "html.parser")

comment = soup.findAll(text=lambda text:isinstance(text, Comment))[0]
comment = ''.join(comment.split())

# Use regular expressions to match the string format.
# Clue: "One small letter, surrounded by EXACTLY three big bodyguards on each
# of its sides."
a = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')

# Print the middle character.
for each_match in a.findall(comment):
    sys.stdout.write(each_match[4])
sys.stdout.write('\n')
