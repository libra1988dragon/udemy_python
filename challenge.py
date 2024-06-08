# 문자열을 입력 받은 후 그 문자열의 길이 구하기 
# input함수를 사용해서 먼저 문자열의 입력 받은 후 
# len함수의 매개변수로 입력받은 문자열이 들어와서 총 길이가 print함수에 의해 출력된다.
# print(len(input()))

# 밴드 이름 생성 프로그램을 만드시오
# 사용자로부터 자란 도시와 기르고 있는 애완동물의 이름을 입력 받은 후 
# 그 이름들을 결합하여 밴드 이름을 생성하는 프로그램을 만드세요

# print("환영합니다. 밴드 이름 생성기 입니다.")
# city_name = input("당신이 자란 도시의 이름은 ??\n")
# pet_name = input("당신이 기르고 있는 애완동물의 이름은??\n")
# band_name = city_name + " " + pet_name
# print("밴드 이름은 " + band_name + " 입니다.")

# input함수로 두수를 입력받는다.
# ex) 34를 입력받아서 3 + 4 의 값이 출력되도록 코드를 완성하시오
# num = input("두자리 숫자를 입력하세요\n")
# sum_value = int(num[0]) + int(num[1])
# print(sum_value)

# BMI 계산
# BMI = 몸무게(kg) / 키의 제곱 
# 먼저 키를 입력 받습니다. m단위로 1.8
# 그 다음 몸무게를 입력받습니다. kg단위 
# 두 수를 입력받아 bmi를 구하세요 단 bmi는 정수입니다.

# height = input("당신의 키를 입력해주세요 (단위는 m입니다.) ex) 183cm 일경우 1.83을 입력해주세요. \n")
# weight = input("당신의 몸무게를 입력해주세요 (단위는 kgd입니다.) ex)80kg 일경우 80입력해주세요 \n")

# float_height = float(height)
# int_weight = int(weight)

# bmi = int_weight / (float_height ** 2)
# int_bmi = int(bmi)
# print(int_bmi)


# 나이를 입력 받고 90살까지 산다고 가정했을 때 앞으로 얼만큼 시간이 남았는지 표현하기
# 단위는 주(weeks)
# # 참고로 1년은 52주 
# age = input("당신의 현재 나이는 얼마 입니까?") 
# max_age = 90
# my_life_time = max_age - int(age)
# my_life_time_weeks = my_life_time * 52
# print(f"현재 저의 나이는 {age}이며 {max_age}까지 {my_life_time}년 남았고 주로는 {my_life_time_weeks}주 남았습니다.")


# 팁 계산기

# print("팁 계산기 입니다.")
# bill = float(input("음식값은 $"))
# tip_percent = input("팁을 몇프로 주시겠습니까? 10, 12, 15 중에 하나를 선택해주세요")
# float_tip_percent = int(tip_percent) / 100
# people = input("인원 수를 입력해주세요")
# int_people = int(people)
# tip = bill * float_tip_percent 
# total_bill = bill + tip
# per_total_bill = round(total_bill / int_people, 2)
# print(f"1인당 계산 해야할 금액은 {per_total_bill}) 달러입니다.")


# print("롤로코스터에 오신걸 환영합니다.")
# height = int(input("손님 키가 어떻게 되시나요?? cm로 입력해주세요"))

# if height > 120:
#     print("롤러코스터 탑승이 가능하십니다.")
#     age = int(input("나이를 입력해주세요 \n"))
#     if age < 12:
#         print("요금은 3000원입니다.")
#     elif age < 20:
#         print("요금은 5000원입니다.")
#     else:
#         print("요금은 7000원입니다.")
# else:
#     print("아쉽지만 롤러코스터 탑승불가 입니다.")

# 윤년 계산기
# 조건 4로 나눠서 나머지가 없어야하고
# 조건 100으로 나눠서 나머지가 없으면 안되고
# 조건 400으로 나눠서 나머지가 없으면 안됨

# year = int(input("년도를 입력해주세요\n"))
# if year % 4 == 0: 
#     if(year % 100 == 0):
#         print(f"{year}은 윤년이 아닙니다.")
#     elif(year % 400 == 0):
#         print(f"{year}은 윤년이 아닙니다.")
#     else:
#         print(f"{year}은 윤년이 맞습니다.")
# else:
#     print(f"{year}은 윤년이 아닙니다.")    

# bill = 0
# print("어서오세요 파이썬 피자입니다.")
# pizza_size = input("사이즈는 어떻게 하시겠습니까? S,M,L 중 하나를 선택해주세요\n")
# if(pizza_size == "S"):
#   print("Small 사이즈 피자는 $15달러 입니다.")
#   bill += 15
# elif(pizza_size == "M"):
#   print("Medium 사이즈 피자는 $20달러 입니다.")
#   bill += 20
# else:
#   print("Large 사이즈 피자는 $25달러 입니다.")
#   bill += 25
# add_peperoni = input("페퍼로니를 추가하시겠습니까? Y/N\n")
# if(add_peperoni == "Y"):
#   if(pizza_size == "S"):
#     bill += 2
#   else:
#     bill += 3
# add_extra_cheese = input("엑스트라 치즈를 추가하시겠습니까? Y/N\n")
# if(add_extra_cheese == "Y"):
#   bill += 1
# print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}.") 


# 사랑 계산기
# lower(), count() 함수
# 사용자로 부터 두가지 이름을 받아서 그 이름 안에 t,r,u,e 의 횟수를 총 더해서 앞자리
# l,o,v,e의 횟수를 총 더해서 뒷자리를 가지는 lovescore를 가지고
# 점수별로 출력되는 계산기를 만드시오
# Angela Yu
# Jack Bauer 넣었을 떄 love_score가 53이 나와야한다.

name1 = input("What's your name?\n")
name2 = input("What's your name?\n")

combine_name = name1.lower() + name2.lower()
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")

first_love_score = str(t + r + u + e)

l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")

second_love_score = str(l + o + v + e)

love_scroe = int(first_love_score + second_love_score)

if(love_scroe < 10 or love_scroe >= 90):
    print(f"Your score is {love_scroe}, you go together like coke and mentos.")
elif(love_scroe >= 40 and love_scroe >= 50):
    print(f"Your score is {love_scroe}, you are alright together.")
else:
  print(f"Your score is {love_scroe}.")

    