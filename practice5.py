#print("Pytyon", "Java", "JavaScript", sep=" , " , end = "?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=" : ")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0:>+10}".format(500))
# print("{0:>+10}".format(-500))
# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# #3자리마다 콤마를 찍어주기
# print("{0:,}".format(10000000000000))
# #3자리마다 콤마를 찍어주기, +-부호도 붙이기
# print("{0:+,}".format(10000000000000))
# #3자리마다 콤마를 찍어주기, +-부호도 붙이기, 자릿수 확보 빈자리는 ^ 로 채우기
# print("{0:^<+30,}".format(10000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정자리수 까지만 표시 (소수점 셋째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# score_file = open("score.txt","w", encoding="utf8") # "w"는 쓰기. 덮어쓰기 됨
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽는다. 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="") # 줄 바꾸기 안하려면 
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

import pickle
# profile_file = open("profile.pickle","wb") # b:binary
# profile = {"이름":"박명수","나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb") 
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with open("profile.pickle","rb") as profile_file: # close하지 않고 끝낸다.
#     print(pickle.load(profile_file))  

# with open("study.txt","w", encoding="utf8") as study_file: 
#     study_file.write("파이썬을 열심히 공부하고 있어요.")    

with open("study.txt","r", encoding="utf8") as study_file: 
    print(study_file.read())        