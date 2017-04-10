# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-

the_count =[1, 2, 3, 4, 5] # 리스트
fruits = ['apples', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes' ,3, 'quarters' ]

#this first kind of for - loop goes through a list
for number in the_count:
    print"This is count %d" % number#변수

#same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# alos we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
    print("I got %r "% i)

#we can also buld lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)
# range 정수의 등차수열을 만들어 주는 역할을 한다.
# 또는 python 에서는 아래와 같이 할 수도 있다
#list comprehension

#now we can print them out too
for i in elements:
    print("Element was: %d " %i)


#for는 여러번 실행 여러개의 자료를 추출핤 수 있다.
