#!/usr/bin/env python

import urllib2
from StringIO import StringIO
from zipfile import ZipFile

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
fpath = "/home/richard/development/exercises/python_challenge/6_dir/"

# Download and unzip the file.
zip_file = ZipFile(StringIO(urllib2.urlopen(url).read()))

# There's a README in the extracted set of files.
# It says to start from file "90052.txt".
next_value = "90052"

# We'll need to grab the comments from all the members of the archive.
comments = []
while True:
    try:
        raw_data = zip_file.read(next_value + ".txt")
        next_value = raw_data.split()[-1]
        comments.append(zip_file.getinfo(next_value + ".txt").comment)
    except:
        break
print "".join(comments)
