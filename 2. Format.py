# Format.py

'''
    문자열 기본 포매팅
        - 문자열 안에 '값'을 '삽입'하는 방법

        - 포맷코드 (서식문자)
            %c : 문자 1개
            %s : 문자열
            %d : 정수
            %f : 실수
            %% : % 하나 문자로 사용            
'''


# 문자열 기본 포매팅

# 아이폰12의 가격은 200만원 입니다.
print("아이폰", 12, "의 가격은", 200, "만원 입니다.")
print("아이폰%d의 가격은 %d만원 입니다." % (12, 200))
# "서식문자1 서식문자2 ..." % (값1, 값2, ...)

str1 = "정수는 %d입니다." % (100)
print(str1)

print("실수는 %f입니다." % (10.123))
print("정수는 %d입니다."% (30.12))
print("실수는 %f입니다." % (20))

print("문자열은 %s입니다." %("나는 문자열이다!"))
print("문자열은 %s입니다."%("A"))
print("문자열은 %s입니다."%(30))
print("문자열은 %s입니다." %(10.123))

num1 = 10
num2 = 20
print("10 + 20의 결과는 %d 입니다." % (num1 + num2))
print()

print("미세먼지 농도가 99%입니다.")
print("미세먼지 농도가 %d%%입니다."%(99))
# 문자열 포매팅을 사용하지 않으면 %기호는 일반 문자로처럼 사용
# 포매팅을 사용하면 %하나를 사용하고 싶을 때 두번 써야 한다. %%


'''
     복합 대입 연산자
         > 대입연산자(=)와 다른 연산기호가 합쳐진 형태
         > 자기자신의 값을 이용해서 연산 후, 나한테 다시 대입

    +=   -=   *=   /=
     
'''

num = 10

num += 10 # num = num + 10
print("num =", num)

num -= 5 # num = num - 5
print("num =", num)

num *= 3 # num = num * 3
print("num =", num)

num /= 5 # num = num / 5
print("num =", num)

# 포맷코드를 활용한 소수점 표현
print("소수 : %f" % 10.1) # 기본 6자리
print("소수 : %f" % 10.6666666666) # 자동 반올림
print("소수 : %.0f" % 10.6666666666) # 소수점 지정 %.자리수f 반올림처리
print()

# 정렬과 공백
print("[%s] [%s]" % ("파이썬", "재밌다"))
print("[%10s] [%10s]" % ("파이썬", "재밌다")) # %(숫자)서식문자
                                            # 삽입 시 10칸 확보 후 값을 넣겠다.
                                            
print("[%-10s] [%-10s]" % ("파이썬", "재밌다")) # 좌측정렬


'''
    슬라이싱 이용하여 name변수에 "유재석"을 대입, gender 변수에 "남자"를 대입하여 출력
    info = "유재석 - 남자"
    name = 
    gender = 
'''
info = "유재석 - 남자"
name = info[0:3]
gender = info[-2:]
print(name)
print(gender)
print()
"""
    이름, 나이, 전화번호를 변수로 만든 뒤 출력(기본 포매팅으로 출력)

    [출력결과]
    이름 : 유재석
    나이 : 30세
    전화번호 : 010-1234-5678
    
"""

name = "유재석"
age = 30
phone = "010-1234-5678"

# "    " % ()
print("이름 = %s" %name)
print("나이 = %d" %(age))
print("전화번호 = %s" %(phone))
print()

print("이름 = %s\n나이 = %d\n전화번호 = %s" %(name, age, phone))





