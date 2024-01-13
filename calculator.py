# 간단한 계산기 스크립트

# 숫자 입력 받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 연산자 입력 받기
operator = input("사용할 연산자를 입력하세요 (+, -, *, /): ")

# 계산 수행
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "0으로 나눌 수 없습니다."
    else:
        result = num1 / num2
else:
    result = "유효하지 않은 연산자입니다."

# 결과 출력
print(f"결과: {result}")

