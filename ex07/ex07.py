# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
print " 한글패치"

print "Mary had a little lamb."
print  "Its fleece was white as %s." % 'snow'
print "And everywhere that Marry went"
print "." * 10 # What`d that do
#"."를 10개 복사 한것이다.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that cmma at the end.  try removing it to see what happens
# 쉼표를 제거해봐라 무슨일이 일어나는지
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# ",를 붙이면 Cheeses Burger가 되고 ,를 제거하면 Cheese-Burger가 된다 (-는 다음 문장부터) "
# 위에 순서가 틀려도 아래순서가 맞으면  Cheeses Burger가 그대로 나오게 된다.