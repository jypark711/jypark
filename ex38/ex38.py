# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy" ]

print (stuff)

while (len(stuff)) != 10 : # !은 아니다 라는 의미다 같지 않다라는 의미이다.
    next_one = more_stuff.pop()
    print("Addings: %s" % next_one)
    stuff.append(next_one)
    print("There as %d items now." % len(stuff))


