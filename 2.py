#! /usr/bin/env python

# http://www.pythonchallenge.com/pc/def/ocr.html

from bs4 import BeautifulSoup, Comment
import urllib
import collections

page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
soup = BeautifulSoup(page.read(), "html.parser")

# Get all the comments from the page.
comments = soup.find_all(string=lambda text:isinstance(text, Comment))

# Count the occurences of each character using a dict.
d = collections.defaultdict(int)
for c in comments[1]:
    d[c] += 1

# Output the characters.
for c in sorted(d, key=d.get):
  print '%s %6d' % (c, d[c])
