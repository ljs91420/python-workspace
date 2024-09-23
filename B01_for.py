# B01_for.py

# 파이썬의 for문은 forEach와 유사하다.

# [] : 파이썬의 리스트
for x in [1, 2, 3, 4, 5]:
    print(x);

for animal in ['tiger', 'lion', 'horse', 'rabbit', 'dog', 'cat']:
    print(animal);

# 원하는 범위의 숫자 리스트 객체를 생성하여 반환하는 함수
print(range(10));

for num in range(10):
    print(num);

for num in range(5, 10):
    print("n2:", num);

for num in range(15, 55, 2):
    print("n3:", num);

for num in range(100, 80, -3):
    print("n4:", num);

# 문자열로도 for문을 돌릴 수 있다.
for ch in "안녕하세요 오늘은 파이썬 수업입니다.":
    print(ch);

# break, continue 활용
for ch in "a1b2c3d4e5f6g7":
    if not (ch < '0' or ch > '9'):
        continue;
    print(ch);

for num in range(100):
    if num == 3:
        break;
    print(num);

# 구구단 2단 ~ 9단까지 출력해보기
for dan in range(2, 10):
    print("#### %단 ####" % dan);
    for gop in range(1, 10):
        print("%d * %d = %d" % (dan, gop, dan * gop));