# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
print " 한글패치"

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goob bye?!"
target.truncate()

print "Now I'am going to ask you three lines."

line1 = raw_input("line 1:you ")
line2 = raw_input("line 2:you ")
line3 = raw_input("line 3:you ")

print "l'm going to write these to the file "

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

