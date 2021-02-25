# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
#print(cabinet.get(3))
# print(cabinet.[5])
#print(cabinet.get(5))



# 새 손님
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"]
# print(cabinet)

# #key 만 출력
# print(cabinet.keys())

# #value 만 출력
# print(cabinet.values())

# #key , value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐정
# cabinet.clear()
# print(cabinet)

#menu = ("돈까스", "치즈까스")
#print()

# 집합 (set)
# 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석","박명수"])

# # 교집합 (java와  python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# #합집합 (java 할 수 있거나  python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python을 할 수 없는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

# 자료구조의 변경
# 커피숍
menu = {"커피","우유","쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))