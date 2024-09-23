# A01_DataTypes.py

print("문자열");
print('문자열');
print("문자\n열");
print("문자\t열");
print("\"문자열\"");

print(123 + 123);
print(123 * 123);
print(2 ** 10); # **로 제곱을 할 수 있음

print(123 / 10); # 그냥 나누면 실수
print(123 // 10); # //로 나누면 몫을 구함

print(True);
print(False);

print(True and True);
print(True and False);
print(True or True);
print(True or False);

print(type(123));
print(type(123.123));
print(type(True));
print(type("123"));
print(type('123'));
print(type("""
      모양이 유지되는
      문자열입니다.
"""));

# 문자열 + 숫자가 자바랑 다르다.
print("나이 : " + str(32));
print(int('55') + 10);
print(float('55') + 10);