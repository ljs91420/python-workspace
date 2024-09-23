# C00_def.py

# 함수 만들기

def isNum(ch):
    return '0' <= ch <= '9'

print(isNum('한'))
print(isNum('9'))

# 사과 바구니 함수
def calcAppleBasket(qty, size):
    return qty // size if qty % size == 0 else qty // size + 1
    # return qty % size == 0 ? qty // size : qty // size + 1

print(calcAppleBasket(55, 10))
print(calcAppleBasket(50, 10))

# *매개변수는 여러 개의 인자값을 튜플 타입으로 받는 매개변수가 된다.
# 가변길이 매개변수는 매개변수의 맨 뒤에만 선언할 수 있다.
def printAllMessage(teller, *messages):
    for msg in messages:
        print(teller, ":", msg)
    # print(messages)
    # print(type(messages))

printAllMessage("나", "안녕하세요", "ㅎㅇ요", "랜덤 고르셨네요", "종족이 뭐예요?")
printAllMessage("상대", "종족은 비밀입니다.", "gg요")

# **매개변수는 개수가 정해지지 않은 인자값들을 딕셔너리 형태로 묶어서 전달받는 가변길이 매개변수가 된다.
def printStudentInfo(**student):
    print(student)
    print(type(student))
    print(student['name'])
    print(student['age'])
    print(student['school'])

printStudentInfo(age=10, name='최철수', school='노량진초등학교')

# 함수 선언시에 매개변수에 값을 미리 대입해놓으면 기본값이 된다.
def sum(a = 0, b = 0):
    print("전달하신 두 수의 합은", a + b, "입니다.")

sum()
sum(1)
sum(1, 10)

# 함수에 값을 전달할 때 매개변수명을 정확히 입력하면 순서를 무시하고 전달할 수 있다.
def minus(a = 0, b = 0):
    print("전달하신 두 수의 차는", a - b, "입니다.")

minus()
minus(10)

# 매개변수의 순서를 무시하고 인자값을 전달할 수 있다.
minus(b = 10)
minus(b = 10, a = 3)