#1번 퀴즈
# age = int(input("나이가 어떻게 되십니까?"))
# print(f"나이가 {age}살이라면, 출생년도는 {2025 - age}년입니다.")
#
# #2번 퀴즈
# side = int(input("한 변의 길이:"))
# print(f"한 변의 길이가 {side}cm이면, 넓이는 {side ** 2}cm^2 입니다.")
#
# #3번 퀴즈 밑변과 높이
# base = int(input("밑변의 길이:"))
# height = int(input("높이의 길이:"))
# print(f"밑변 {base}와 높이 {height}의 정삼각형의 넓이는 {base*height*0.5}입니다.")


num = int(input("10000~99999 사이 정수 입력:"))
ten_thousands = num // 10000
thousands = (num % 10000) // 1000
hundred = (num % 1000) // 100
ten = (num % 100) // 10
one = (num % 10)
print(f"{ten_thousands}만 {thousands}천 {hundred}백 {ten}십 {one}")

time = int(input("시간 입력:"))
hour = time // 3600
min = (time % 3600) // 60
sec = time % 60
print(f"{hour}시 {min}분 {sec}초")

num1 = int(input("10000~99999 사이 정수 입력:"))
print(f"{(num1 // 100) % 10}")