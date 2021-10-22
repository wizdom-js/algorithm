import sys
sys.stdin = open('input.txt')


def binary_search(num):
    s = 1
    e = len(lis)-1
    while s <= e:
        m = (s + e) // 2
        if lis[m] == num:
            return m
        elif lis[m] < num:
            s = m + 1
        else:
            e = m - 1
    return s
    # num은 lis 안의 숫자 중, num보다 한 단계 큰 숫자의 자리에 들어간다.


n = int(input())    # 수열의 크기
arr = list(map(int, input().split()))   # 수열

lis = [0]    # 증가하는 수열을 담는 리스트 (인덱스 에러 때문에 0으로 채워준다.)
for num in arr:         # 입력받은 수열의 숫자들을 하나씩 가져온다.
    if lis[-1] < num:    # lis의 마지막 숫자는 lis에서 가장 큰 숫자이므로, lis 안의 가장 큰 숫자보다 num이 크다면
        lis.append(num)  # 증가하는 것이므로 추가해준다.
    else:
        lis[binary_search(num)] = num    # 그렇지 않다면 이진탐색으로 lis에 들어갈 자리를 정해준다.

print(len(lis)-1)    # 맨 처음 0을 담고 시작했으므로, lis의 길이 -1해준다.

