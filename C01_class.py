# C01_class.py

class Fruit:
    # static 영역
    RED = 0
    GREEN = 1
    PURPLE = 2

    @staticmethod
    def calc(fruit, qty):
        print('해당 과일 %d개 구매시 총 가격은 %d원입니다.' % (qty, fruit.price * qty))

    # __init__() 메서드
    # - 생성자
    # - 첫 번째 인자값으로 self를 받아야 한다.(this 역할)
    # - self에 선언한 변수들이 인스턴스 변수가 된다.
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printInfo(self):
        print('%s의 가격은 %d원입니다.' % (self.name, self.price))

f1 = Fruit('사과', 2000)
f2 = Fruit('샤인 머스켓', 3500)

f1.printInfo()
f2.printInfo()

# 해당 클래스의 static값 활용하기
print(Fruit.RED)
print(Fruit.GREEN)
print(Fruit.PURPLE)

# 해당 클래스의 static 메서드 활용하기
Fruit.calc(f1, 5)
Fruit.calc(f2, 17)