# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
print " 한글패치"

from sys import argv

script, filename = argv
print ("argv ="  +str(argv))
txt = open(filename)

print "Here`s your file %r:" % filename
print txt.read()

print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print txt.close()