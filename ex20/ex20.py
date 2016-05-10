# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
from sys import argv

script, input_file = argv

def print_all(f):
    print (f.read())

def rewind(f):
    f.seek(0)
# seek는 파일을 접근 할때 사용하는것으로 줄 단위로 접근하는것이 아니라 byte 단위로 접근을
# 한다 seek(0)는 0byte의 위치로 이동한다는 것이다.
def print_a_line(line_count, f):
    print (line_count, f.readline())

current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)

print ("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


# +=은 무엇을 뜻하냐면  x = x + y , x+= y