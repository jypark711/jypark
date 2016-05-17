# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-

if "raw_input" not in dir(__builtins__):
    raw_input = input
#builtins?
print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = raw_input(">")

if door =="1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print"1. Take the cake."
    print"2. Scream at the bear"

    bear = raw_input(">")

    if bear == "1":
        print("The bear eats you face off. Good job ")
    elif bear == "2":
        print("The bear eats you legs off. Good job")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You share into the endless abyss at cthulhu`s reina.")
    print("1. Blueberries.")
    print("2. Yeollow jaket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of munk. Good job! ")

else:
    print("You stumble around and fall on a knife and die. Good job!")