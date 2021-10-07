# 두글자씩 끊은 다중집합 만들기
def make_set(str):
    str_set = []
    for i in range(len(str) - 1):
        temp = str[i:i + 2]  # 두글자씩 끊기
        if temp.isalpha():  # 기호나 숫자 없다면
            str_set.append(temp)  # 추가
    return str_set


def solution(str1, str2):
    str1 = str1.upper()  # 대소문자 차이 무시하므로 둘다 대문자로 변환
    str2 = str2.upper()

    str1_set = make_set(str1)  # 각 문자열 다중집합으로 만들기
    str2_set = make_set(str2)

    intersection = 0  # 교집합 계산
    for i in str1_set:
        if i in str2_set:
            intersection += 1
            str2_set.remove(i)  # 중복 방지를 위해 삭제

    union = len(str1_set) + len(str2_set)  # 합집합 계산

    if union == 0:  # 합집합 0인경우 1로 처리 -> 65546
        return 65536
    else:
        return int(intersection / union * 65536)


arr = list(range(1, 11))
for i in arr:
    print(i)
    arr.remove(i)

print(arr)