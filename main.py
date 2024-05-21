# # 출력하고 싶은 문자를 따옴표 안에 넣으면 문자가 출력된다. 
# print('Hello world')
# # 여러 줄의 문자열을 출력하고 싶을 경우 
# # 첫번쨰 방법 \n을 사용한다.
# print("Hello world\nHelloworld\nHello world")

# # 두번쨰 방법 """ """ ''' ''' 따옴표 3개를 사용한다.
# print('''
# Hello world
# Hello world
# Hello world
#       ''')

# # 문자열 결합하기
# # 문자열 결합시에는 + 연산자를 사용하여 결합한다.
# print("Hello" + " Dongkyu ")

# # 문자열 공백 넣기
# print("공백 넣기")
# print("공백" + " 넣기")
# print("공백 " + "넣기")
# print("공백" + " " + "넣기")

# print('String Concatenation is done with the "+" sign.')

# # input함수 사용하기 
# # input함수는 사용자가 입력한 내용을 문자열로 나타냄
# print("Hello " + input("What's your name ??"))

# 변수 
# 변수를 사용하지 않고 input() 함수만 사용했을 경우 사용자의 입력은 받지만 값은 할당되지 않아서 아무런 의미가 없다.
# 변수를 사용할 경우 input() 함수로 사용자가 입력한 값이 name 변수에 할당된다.
# name = input("What is your name ??")
# # len함수는 매개변수로 할당된 값의 길이를 숫자형 데이터로 리턴해준다.
# length = len(name)
# # str()함수를 사용한 이유는 length변수의 데이터 타입이 숫자형이고 
# # 파이썬에서 문자열 데이터와 숫자는 함께 사용할 수 없기 때문에
# # str()함수를 사용해서 숫자형 데이터를 문자열로 바꿨다.
# print("내 이름은 " + name + " 이고 글자수는 " + str(length))

