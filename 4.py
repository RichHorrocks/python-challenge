#! /usr/bin/env python

# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib
from bs4 import BeautifulSoup, SoupStrainer

URL_STR = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url_num = "12345"

while True:
    try:
        page = urllib.urlopen(URL_STR + url_num)
        soup = BeautifulSoup(page.read(), "html.parser")
        url_num = str(soup).rsplit(' ', 1)[1]
        print("Trying the next URL: %s" % str(soup).rsplit(' ', 1)[1])
    except:
        break

print("The final page is '%s'" % (URL_STR + url_num))
