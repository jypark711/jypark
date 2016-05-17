# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
people = 30
cars = 40
trucks =15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide.")
#if elif else 등 나올때는표시를 하시오

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trcuks")
else:
    print("We still can't decide")
#

if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's stay home then")

#처음에 if 에서 걸리면 if로 표시 하고 if가 아니라면
#elif 로 넘어간다 elif도 아닐시에는 else로 넘어 간다
#else는 마지막의 여집합 같은 개념으로 생각하면 된다.