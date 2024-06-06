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

# 파이썬 데이터 타입
# 1. String 문자열
# ex) Hello python에서는 큰따옴표나 작은따옴표로 감싸서 표현 'Hello' "Hello" 

# "Hello"라는 문자열에서 o만 추출해서 출력하기
# 이렇게 문자열에서 특정 부분을 추출하는 방법을 서브스크립트(Sub-script)라고 한다.
# 괄호 안에 추출할 문자의 인덱스를 넣으면 되는데 인덱스는 0부터 시작하므로 주의해야한다.
# print("Hello"[4])
# 그렇다면 "123" 은 문자열일까 숫자일까? 정답은 문자열이다.
# 무조건 따옴표 안에 들어간 숫자나 문자는 모두 문자열이다.
# "123" + "456" 도 문자열 + 문자열 덧셈을 하는게 아니라 
# 문자열 결합 연산자이므로 123456이다.
# print("123" + "456")

# 2. Integer 정수형
# 정수형은 말그대로 숫자만 있는 형태이다.
# print(123 + 456)
# 현실에서 큰 수를 나타낼 때 3자리 마다 ,(콤마)를 넣어 표현하는데
# 파이썬에서는 큰 수를 나태낼 떄 _(언더바)를 사용한다. _바는 주석처럼 완전히 무시되기 떄문에 편하게 사용해두 된다.
# 123_456_789

# 3. 실수형 Float
# print(3.14)

# 4. Boolean 
# True False

# 타입 오류와 형변환
# 실행시 변수 num_char의 값이 문자열이 아니라 int형이라 에러가 발생한다.
# 그 이유는 len함수는 int값을 리턴하기 때문이다.
# 파이썬에서 string과 int는 결합연산자로 결합을 할 수 없다.
# 그래서 int를 string형으로 데이터 타입을 바꿔야 하는데 이떄 사용하는게 str함수이다.
num_char = len(input("당신의 이름은 무엇인가요?"))
print(num_char)
print("당신의 이름은 " + num_char + " 글자네여 ")
str_num_char = str(num_char)
print("당신의 이름은 " + str_num_char + " 글자네여 ")
