# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money) : # 출금
#     if balance >= money : # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.",format(balance))
#         return balance

# def withdraw_night(balance, money) : #저녁에 출금
#     commission = 100
#     return commission, balance - money - commission


# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name,age, main_lang))
# profile("유재석", 20, "파이썬")

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name,age, main_lang))
# profile("유재석")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end =" ")
#     print(lang1, lang2, lang3....)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end =" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")

gun = 10


def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))

gun = checkpoint_ret(gun, 2)

print("남은 총 : {0}".format(gun))
