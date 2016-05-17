# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-

i = 0
number = []

while i < 6:
    print("At the top i is %d" % i)
    number.append(i)

    i = i + 1

    print("Numbers now: " +str(number))
    print("At the bottom i is %d" % i)

print("The number:")

for num in number:
    print (num)

#while 루프 함수 범위안의 참값을 모두 출력
