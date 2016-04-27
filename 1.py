#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/def/map.html
# This challenge involve a bog-standard Caesar Cypher.
#   https://en.wikipedia.org/wiki/Caesar_cipher

import string
import sys
import urllib
from bs4 import BeautifulSoup

page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/map.html")
soup = BeautifulSoup(page.read(), "lxml")
words = soup.find(color="#f000f0").string

# The Caesar Cypher algorithm is thus:
#   E(x) = (x + n) % 26
#    where n is the shift

lc_letters = string.lowercase

for each_letter in words:
    try:
        i = lc_letters.index(each_letter)
        # Our cypher has a shift of 2.
        sys.stdout.write(lc_letters[(i + 2) % 26])
    except:
        sys.stdout.write(each_letter)

# Ugh. Solution suggests using string.maketrans()... :)
