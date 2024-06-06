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