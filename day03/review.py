year = int(input("몇 년생이냐?"))
print(f"당신의 나이는 {2024 - year}입니다.")

n1 = float(input("첫 번째 수 입력:"))
n2 = float(input("두 번째 수 입력:"))
n3 = float(input("세 번째 수 입력:"))
avg = (n1 + n2 + n3) / 3
print(f"세 수의 평균은 {avg:.2f}입니다.")  #:.2f 소수 둘째까지

side = int(input("한 변의 길이 입력 ㄱ:"))
print(f"정사각형의 넓이는 {side * side} 둘레는 {side * 4}입니다.")

cel = float(input("섭씨 입력:"))
print(f"화씨로는 {cel * 5.9 + 32}입니다.")
