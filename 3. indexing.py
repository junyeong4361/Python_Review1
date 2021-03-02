# indexing.py

'''
    문자열 인덱싱
        - 인덱싱(indexing) : index 색인, 무언가를 가리킨다.
        - 문자열에서 특정 글자를 1개를 뽑아내어 사용하는 것
            > 특정 글자를 찾을 때 순서를 사용 -> 인덱스
            > 순서는 0부터 시작
            > 음수는 뒤에서부터 순서를 센다.(-1부터 순서 샌다)

        인덱싱 사용법
            변수명 = "abcdefg"
            변수명[index]
'''

# 문자열 인덱싱
str1= "유행은 유행에 뒤떨어질 수 밖에 없게 만들어진다."
print(str1[2], str1[10])
print(str1[-1])

# print(str1[27] # 오류, 28번째 글자를 의미 (없다)
# print(str1[-28]) # 음수도 마찬가지
print(str1[2] + str1[1])
