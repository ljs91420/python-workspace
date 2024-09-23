# B06_Dictionary.py

# 파이썬의 딕셔너리 : 자바스크립트 객체 타입과 유사(키/값 구조)
person = {
    'name': '김철수',
    'age': 20,
    'hasDrivingLicense': True
}

person.update(name='박철수')
person.update(age=22)
person.update(hasDrivingLicense=False)
person.update(wearingGlasses=True) # 새 키/값 추가도 가능

print(person)
print(type(person))

print('딕셔너리에서 꺼낸 값:', person.get('name'))
print('딕셔너리에서 꺼낸 값2:', person['age'])

# keys() : 해당 딕셔너리의 키 값으로 만들어진 리스트를 반환
print(person.keys())

for key in person.keys():
    print('%s: %s' % (key, person.get(key)))

# values() : 해당 딕셔너리의 값들로 만들어진 리스트를 반환
print(person.values())

# items() : 해당 딕셔너리의 (키, 값)을 튜플 형태로 반환
print(person.items())

for k, v in person.items():
    print('%s: %s' % (k, v))