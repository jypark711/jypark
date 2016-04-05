# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
print " 한글패치"

tabby_cat = "\tI`m tabbed in."
a_tabby_cat = "a\tI`m tabbed in."
persian_cat = "I`m split\non a line."
backslash_cat = "I`m \\ a\\ cat."
#||는 결국에는 하나가 표시가 괸다. \t는  공백을 생기게 한다.
fat_cat = """
I`ll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#\_Escape Seguence
print tabby_cat
print a_tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print('%r' % "single quote \' double quote \"")
print('%r' % "single quote \" double quote \'")