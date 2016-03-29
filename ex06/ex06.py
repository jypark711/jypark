# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
print " 한글패치"
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y
# %r은 X의 내용을 전부다 표시하는 것이 아니라 X안의 %()의 내용을 표시한다.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
# %로 문자를 나열 사용할 수 있다.
w = "This is the left side of..."
e = "a string with a right side."

print w + e
#문자 삽입 + 는 문자 나열 할때 사용
#문자를 삽입할때는 %라 +랑 큰 차이를 보이지 않는다.
#Debug도 차례 보이기등 다양한 기능을 가지고 있으니 한번 해보자