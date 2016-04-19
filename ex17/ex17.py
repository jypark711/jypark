# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
print " 한글패치"

from sys import  argv
frm os.path import exists

script, from_file, to_file =argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?"
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long") % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to contiune, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
