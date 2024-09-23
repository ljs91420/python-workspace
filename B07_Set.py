# B07_Set.py

# Set
# - 집합을 구현한 자료구조
# - 요소의 중복을 허용하지 않는다.
# - 딕셔너리와 Set 모두 중괄호를 사용하므로 헷갈리지 않도록 주의해야 한다.

animalSet = {'cat', 'cat', 'mouse', 'cow', 'dog', 'pig', 'pig', 'cow'}

print(animalSet)
print(type(animalSet))

numberList = [1, 2, 2, 3, 4, 5, 6, 13, 13, 19, 21, 23, 23, 23, 1, 1, 1]
numberSet = set(numberList)

print(numberSet)

# 중복없는 1 ~ 45의 7자리 랜덤 숫자를 만들어보세요.
import random

print(random.randrange(1, 46)) # 1 ~ 45의 랜덤 정수 생성하기

randomNumberSet = {}

while True:
    random_number = random.randrange(1, 46)
    randomNumberSet.update(random_number)

print(randomNumberSet)