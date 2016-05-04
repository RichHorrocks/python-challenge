#! /usr/bin/env python

# http://www.pythonchallenge.com/pc/def/peak.html

import sys
import pickle
import urllib2

URL = "http://www.pythonchallenge.com/pc/def/banner.p"

# Open the URL in binary format.
handle = urllib2.urlopen(URL, "rb")
pickle_object = pickle.load(handle)
handle.close()

# 'pickle_object' is basically a list of items. 
# Each item looks like the below:
# 
#   [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)],
#
for item in pickle_object:
    for i in item:
        sys.stdout.write(i[0] * i[1])
    print("")
