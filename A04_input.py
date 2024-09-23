# A04_input.py

# input() : 콘솔에서 입력을 받는 함수, 입력을 문자열 타입으로 받는다.
print("16진수로 변환하고 싶은 숫자 입력 >> ", end="");
value = input();

print("입력하신 숫자의 16진수 버전은 %X입니다." % int(value));

# input() 내부에 문자열을 전달하면 안내문(prompt)이 된다.
input("이번에는 8진수로 변환하고 싶은 숫자 입력 >> ");

print("입력하신 숫자의 8진수 버전은 %o입니다." % int(value));