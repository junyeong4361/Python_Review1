# string_function.py

'''
    문자열 관련 함수
        문자열.함수() 형태로 사용
        > 기존 값을 이용해서 새로운 결과를 만들어 낸다.
        > 기존 값은 변화가 없다.(문자열은 변경불가능)
'''


# upper() : 문자열의 영문을 모두 대문자로 변환하여 새로운 문자열을 만든다.
# lower() : 소문자로

str1 = "I'm a Boy"
print(str1.upper())
print(str1)
str2 = str1.lower()
print(str2)
print()

# title() : 문자열에 존재하는 '영단어'의 첫 글자를 대문자로 변경
str3 = "he not busy being born is busy dying."
print(str3.title())
print()

# strip() : 문자열 좌우측에 존재하는 '공백'을 제거
str4 = "    공 백 제 거    "
print(str4.strip())
print()

# join(): 특정 문자열을 대상 문자열에 삽입
print("!". join("join"))
#앞의 문자열을 뒤에 나오는 문자열 사이사이에 삽입
print()

# count("A") : 문자열에서 "A"의 개수를 반환 (정수)
str5 = "he not busy being born is busy dying."
print("str5에서 b의 개수 :", str5.count("b"))
# 찾지 못하면 0

# replace("A","B") : 문자열에서 모든"A"를 찾아서"B"로 변경
str5 = "he not busy being born is busy dying."
print(str5.replace("busy", "바쁘다"))
str4 = "    공 백 제 거    "
print(str4.replace(" ", ""))
print()

# split("A") : 문자열을 기준 문자("A")로 나눈다. (엄청 중요)
str6 = "문자열 나누기 split()"
print(str6.split())
# 기준 문자를 따로 작성하지 않으면 기본이 공백, 개행 등으로 나눈다.
# 반환 하는 값은 뒤에 배울 리스트 자료형
# 기준되는 문자는 포함x
print(str6.split("나누기"))
print()

# index("A") : 문자열에서 "A"를 찾고, 그 위치를 반환 (찾지 못하면 오류)
str7 = "문자열 위치 찾기! index"
print("str7에서 !의 위치 :", str7.index("!"))
print("str7에서 !의 위치 :", str7.index("index")) # 찾은 단어의 첫 위치
#print(str7.index("z"))

# find("A") : index와 같다. (찾지 못하면 -1을 반환)
print("abcdefg".find("c"))
print("abcdefg".find("z"))

str5 = "he not busy being born is busy dying."
print(str5.find("busy"))
print(str5.rfind("busy"))

str5 = "he not busy being busy born is busy dying."

print(str5.find("busy", 8))

# index, find의 차이점 : 없을 때 오류가 나고 안나고

'''
    1. 주어진 문자열에서 단어의 첫글자를 대문자로 만들어라!
        my_str = "strong reasons make strong actions."
'''
# 1.
my_str = "strong reasons make strong actions."

print(my_str.title())

print()

'''
    2. 주어진 문자열에서 "시든" 이라는 단어의 개수는 ?
        """아무말도 아무것도 여전히 넌 여기 없고 널 원하고 널 원해도 난 외롭고
        꽃이 피고 진 그 자리 끝을 몰랐었던 맘이 깨질 것만 같던 그때 우리 음 시든 꽃에
        물을 주듯 싫은 표정조차 없는 결국엔 부서진 여기 우리 음 다 잊었니 말없이 다 잊었니
        사랑한단 말로 날 가둬둔 채로 넌 잊었니 난 잊지 못하나봐 바보처럼 기다려 난 오늘도
        어쩌다 이렇게 됐지 너무 예뻤잖아 둘이 매일 설레였지 그때 우린 음
        시든 꽃에 물을 주듯 싫은 표정조차 없는 결국엔 부서진 여기 우리"""
'''
# 2.
str10 = """아무말도 아무것도 여전히 넌 여기 없고 널 원하고 널 원해도 난 외롭고
        꽃이 피고 진 그 자리 끝을 몰랐었던 맘이 깨질 것만 같던 그때 우리 음 시든 꽃에
        물을 주듯 싫은 표정조차 없는 결국엔 부서진 여기 우리 음 다 잊었니 말없이 다 잊었니
        사랑한단 말로 날 가둬둔 채로 넌 잊었니 난 잊지 못하나봐 바보처럼 기다려 난 오늘도
        어쩌다 이렇게 됐지 너무 예뻤잖아 둘이 매일 설레였지 그때 우린 음
        시든 꽃에 물을 주듯 싫은 표정조차 없는 결국엔 부서진 여기 우리"""
print(str10.count("시든"))
'''
    3. "가나다라마바사아자차카타파하" 에서 문자하나하나를 띄어쓰도록 만들어라!
        [출력결과]
        가 나 다 라 마 바 사 아 자 차 카 타 파 하
'''
# 3.
str11 = "가나다라마바사아자차카타파하"
print(" ". join("가나다라마바사아자차카타파하"))

'''
    4. """자유와 정의 다음으로 중요한 것은 대중 교육인데,
        대중 교육 없이는 자유도 정의도 영원히 유지될 수 없다""" 에서
        "자유"를 모두 찾아 "freedom" 으로 변환하여 출력하라!
'''
# 4.

str12 = """자유와 정의 다음으로 중요한 것은 대중 교육인데,
        대중 교육 없이는 자유도 정의도 영원히 유지될 수 없다"""
print(str12.replace("자유","freedom"))
'''
    5. 문자열 "강력한 이유는 강력한 행동을 낳는다." 에서 "강력"의 개수와
       문자열 "사람 위에 사람 없고 사람 밑에 사람 없다."에서 "사람"의 
       개수는 총 몇 개인가?
'''
# 5.

str13 = "강력한 이유는 강력한 행동을 낳는다."
str14 = "사람 위에 사람 없고 사람 밑에 사람 없다."

print(str13.count("강력"))
print(str14.count("사람"))















