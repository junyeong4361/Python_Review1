# Number.py

"""
    [1. 숫자형]
        정수      : -123, 0, 123
        실수      : -10.123, 123.11
        2진수(binary) : 0b10, 0B10
        8진수(octal)  : 0o10, 0O10
        16진수(hexadecimal) : 0x10, 0X10

[10진수(0 ~ 9)]
    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17

[8진수(0 ~ 7)]
    0   1   2   3   4   5   6   7   10  11  12  13  14  15  16  17  20  21

[16진수(0 ~ 9, a ~ f)]
    0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f   10  11

[2진수(0, 1)]

    128     64      32      16      8       4       2       1



bit : 0 또는 1을 저장할 수 있는 크기
8bit(1byte) : 영문 1글자를 저장할 수 있다.
1024byte(1KB)
1024KB(1MB)
1024MB(1GB)
...

"""

# 기본 숫자형
# print()함수는 숫자를 10진수로 출력해준다.

print("정수 :", -10, 0, 123)
print("실수 :", -1.11, 10.123)
print("2진수 :", 0b10, 0B100, 0b00,0b10000, 0b10101)
print("8진수 :", 0o10, 0O10, 0o11, 0o12, 0o17)
print("16진수 :", 0x10, 0X10)

'''
    사칙연산    : + - * /
    제곱연산    : **
    나머지 연산 : %
    몫 연산     : //  
'''

# 숫자 연산하기
# 연산자 : 연산을 수행하는 '기호'
# 피연산자 : 연산자의 작업대상
# 연산을 수행한다 -> 피연산자를 이용하여 '하나의 값'을 만든다. 

num1 = 10
num2 = 3

print("num1 + num2 =", num1 + num2)
print("num1 - num2 =", num1 - num2)
print("num1 * num2 =", num1 * num2)
print("num1 / num2 =", num1 / num2) # 숫자와 숫자를 나누면 무조건 '실수'
print("num1 ** num2 =", num1 ** num2)
print("num1 % num2 =", num1 % num2)
print("num1 // num2 =", num1 // num2)

# 나머지 연산 %
#   - 두 수를 나누고, 나머지 값만 사용
#   - 12를 3으로 나눈 나머지가 0이면 12는 3의 배수
#   - 어떤 수를 2로 나눈 나머지가 0이면 2의 배수(짝수), 1이면 (홀수)

