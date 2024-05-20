# 출력하고 싶은 문자를 따옴표 안에 넣으면 문자가 출력된다. 
print('Hello world')
# 여러 줄의 문자열을 출력하고 싶을 경우 
# 첫번쨰 방법 \n을 사용한다.
print("Hello world\nHelloworld\nHello world")

# 두번쨰 방법 """ """ ''' ''' 따옴표 3개를 사용한다.
print('''
Hello world
Hello world
Hello world
      ''')

# 문자열 결합하기
# 문자열 결합시에는 + 연산자를 사용하여 결합한다.
print("Hello" + " Dongkyu ")

# 문자열 공백 넣기
print("공백 넣기")
print("공백" + " 넣기")
print("공백 " + "넣기")
print("공백" + " " + "넣기")

print('String Concatenation is done with the "+" sign.')

# input함수 사용하기 
# input함수는 사용자가 입력한 내용을 문자열로 나타냄
print("Hello " + input("What's your name ??"))