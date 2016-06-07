# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
mystuff = {'apple': "I AM APPLES"}
print (mystuff['apple'])

import mystuff
mystuff.apple()
print(mystuff.tangerine)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print ("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)
# object 객체 틀에 맟춰 나오는 것.  Class는 틀을 뜻한다. 변수를 담고 있어야 한다.

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_baby = Song(["Happy birthday to you",
                   "I don`t want to get sued",
                   "So I`ll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With poctets full of shells"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()