# Variable.py

'''
    변수(Variable)
        -값을 저장하는 공간
        -파이썬에서는 값을 '저장'하는 개념이 아니라 값을 '가리킨다'
        
'''
# 프로그래밍 언어에서 =(equal, 등호) 기호는 '같다' 가 아닌 '대입'
# 우측 값을 좌측에 대입

# 변수에 값 대입 (1) - 하나씩
a = 1
b = "hi"
c = 20
#변수를 사용할 때는 그냥 사용한다.
print(a,b,c)
print()

#변수에 값 대입(2) - 한번에
a,b,c = 1,2,3 # 순서대로 대입, 짝이 맞아야 한다.
print(a,b,c)

# 변수에 값 대입(3) - 모두 같은 값
a=b=c=7
print(a,b,c)

# 변수끼리 값 교체
a=1
b=50

a,b = b,a
print(a, b)

'''
    변수명 규칙
        1. 한글 사용 가능 -> 그래도 영어로 한다.
        2. 특수문자(기호)는 _만 사용 가능
        3. 숫자 사용 가능, 단 첫 글자로는 안 된다.
        4. 대소문자 구분
            >변수명 뿐만 아니라, 모든 코드가 구분
            >a, A는 다른 글자

        5. 예약어 사용 불가
            >이미 시스템에서 사용하고 있는 단어
            > 색상이 들어간 단어 사용x

        6. 변수명에 의미를 부여
            ex) 학생의 점수 -> Student_Score
            ex) 사과의 개수 -> Apple_Count
                > a,b,c,d,e,f,g,... (x)

                숫자: num1, num2, num3, ...
                문자열: str1, str2, ...
'''
# 1. 한글 사용 가능
파이썬 = "python"
print(파이썬)

# 2. 특수문자 _만 사용
num_ber = 0
#num@ber = 1

# 3. 숫자 사용, 첫 글자(x)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
n1um = 2

# 4. 대소문자 구분
num=0
NUM=1
Num=2

print(num,NUM,Num)

# 5. 예약어 사용 불가
#import = 1

print = 10 # 변수화가 되었다.
del(print) # del(변수명) -> 해당 변수 제거
print(10)

# 예약어 목록 확인
import keyword
print(keyword.kwlist)

Import = 1
import1 = 2

'''
    이름, 나이, 전화번호 변수 3개에 정보를 대입

    [출력결과]
    이름: 이문규
    나이: 20세
    전화번호 : 010-1234-5678
'''
name="이문규"
age=20
number= "010-1234-5678"

print("이름"+":"+name)
print("나이",":",age,"세", sep="")
print("전화번호"+":"+number)
print()

print("이름:"+name,"\n나이:",age,"세\n전화번호:",number,sep="")









