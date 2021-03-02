# slicing.py

'''
    문자열 슬라이싱
        - 슬라이싱 : 조각내다.
            > 인덱스로 특정 범위의 문자를 조각내서 사용

    str1= "abcdefg"

    str1[0:3] -> 콜론(:)으로 범위 지정

    str1[시작인덱스:끝인덱스] -> 끝인덱스는 포함 안 된다.
    str1[시작인덱스:]        -> 시작인덱스부터 끝까지
    str1[:끝인덱스]          -> 처음부터 끝인덱스까지(끝인덱스는 포함x)
    str1[:]                 -> 시작부터 끝 -> 전체 

            
'''

str1= "He not busy being born is busy dying"
print(str1[7]+str1[8]+str1[9]+str1[10])
print(str1[7:11])

print(str1[:100]) # 인덱스 범위를 초과해도 오류x
print(str1[12:]) # 12부터 끝까지
print(str1[:-8])
print()

# str1에서 첫 글자를 소문자 h로 바꾸고 싶다면
# str1[0] = "h" #파이썬에서는 한번 만들어진 문자열은 수정이 불가능하다.

# 슬라이싱을 이용해서 새로운 문자열을 만들어줘야 한다.
str2 = "h" + str1[1:]
print(str2)
















