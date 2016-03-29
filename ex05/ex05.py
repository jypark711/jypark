# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
print " 한글패치"
name = 'JY.Park박'
age = 23 # not a lie
height_cm = 174.2 # cm
weight_kg = 65 # kg
eyes = 'Black'
teeth = 'White'
hair = 'Black and White'
cm_to_inch = 1.0/ 2.54
height_inch = height_cm * cm_to_inch

print "Let's talk about %s." % name
print "He's %g cm tall." % height_cm
print "He`s %g inch tall" % height_inch
print "He's %d kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)
#Study drill
print "hey your`s name %s? " % name
print "hey your`s name"
#%는 대입 비슷한것이라고 보면 된다.
#%r은 절대로 출력되지 않는다.
#%d 는 숫자열이지만 소숫자리는 버린다 %g는 반면에 소숫자리까지 표시
#%s 는 문자열

