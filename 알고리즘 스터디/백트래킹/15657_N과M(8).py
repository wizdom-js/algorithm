import sys
sys.stdin = open('input.txt')

def recur(cnt, s):
    if cnt == m:
        print(*answer)
        return

    for i in range(s, n):
        answer[cnt] = arr[i]   # 현재 자리 숫자 넣어
        recur(cnt+1, i)         # 다음자리 숫자 찾으러가 근데 현재숫자부터 가능이야


# n개의 자연수 중에서 m개를 고른 수열
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
answer = [0 for _ in range(m)]

recur(0, 0)
