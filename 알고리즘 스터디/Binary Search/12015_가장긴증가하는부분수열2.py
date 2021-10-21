import sys
sys.stdin = open('input.txt')


def binary_search(num):
    s = 1
    e = len(dp)-1
    while s <= e:
        m = (s + e) // 2
        if dp[m] == num:
            return m
        elif dp[m] < num:
            s = m + 1
        else:
            e = m - 1
    return s
    # num은 dp 안의 숫자 중, num보다 한 단계 큰 숫자의 자리에 들어간다.


n = int(input())    # 수열의 크기
arr = list(map(int, input().split()))   # 수열

dp = [0]    # 증가하는 수열을 담는 리스트 (인덱스 에러 때문에 0으로 채워준다.)
for num in arr:         # 입력받은 수열의 숫자들을 하나씩 가져온다.
    if dp[-1] < num:    # dp의 마지막 숫자는 dp에서 가장 큰 숫자이므로, dp 안의 가장 큰 숫자보다 num이 크다면
        dp.append(num)  # 증가하는 것이므로 추가해준다.
    else:
        dp[binary_search(num)] = num    # 그렇지 않다면 이진탐색으로 dp에 들어갈 자리를 정해준다.

print(len(dp)-1)    # 맨 처음 0을 담고 시작했으므로, dp의 길이 -1해준다.

