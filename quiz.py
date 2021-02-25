# (출력예제)
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# --축하합니다--

from random import *
users = range(1,21) # 1부터 20까지 숫자 생성
users = list(users)
shuffle(users)

winners = sample(users,4)
#print(chicken)
#lst.pop(chicken)
print(" --당첨자 발표-- ")
print(" 치킨 당첨자  : {0}".format(winners[0]))
print(" 커피 당첨자  : {0}".format(winners[1:]))
print(" --축하합니다-- ")