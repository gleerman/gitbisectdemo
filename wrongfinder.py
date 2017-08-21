#!/usr/bin/python

filename = "file.txt"
wrongWord = "bad"


if wrongWord in open(filename).read():
    print "The wrong word is present"
    exit(1)
else:
    print "Everything is OK"
    exit(0)
    
