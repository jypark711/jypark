# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
print " 한글패치"
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter %  ( "I had this thing.",
                     "That you could type up right.",
                     "But it didn't sing.",
                     "So I said goodnight.")
# ' 로 인해 "But it didn't sing."이 문장만 ""로 출력   " '안의 다른 문자열로 인식하기 때문에
