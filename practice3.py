# wheather = input("오늘 날씨는 어때요? ")
# if wheather == "비":
#     print("우산을 챙기세요")
# elif wheather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨예요")    
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")    
# else:
#     print("너무 추워요. 나가지 마세요")    

# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨","토르","블랙팬서"]    
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기되었습니다.")

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# absent = [2,5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 옥상으로 따다와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104..
# students = [1,2,3,4,5]
# print(students)
# students = [1+100 for i in students]
# print(students)

