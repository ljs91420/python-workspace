# B03_List.py

prices = [];

# append()로 값을 순서대로 추가
prices.append(10);
prices.append(20);
prices.append(30);
prices.append(40);
prices.append(50);

# 2번째 인덱스에 값 99를 삽입
prices.insert(2, 99);

# 정렬
prices.sort();

prices[0] = 33;

# len() : 길이를 셀 수 있는 객체(해당 클래스의 __len__이 구현된 객체)를 길이를 반환하는 함수
print(len(prices));
print(len("https://naver.com"));

# str() : 문자열로 표현할 수 있는 객체(해당 클래스의 __str__이 구현된 객체)의 문자열 형태를 반환하는 함수
print(str(prices));
print(prices);