import sys
sys.stdin = open('input.txt')


def recur(cnt, s):
    if cnt == m:
        print(*answer)
        return

    for i in range(s, n):
        answer[cnt] = arr[i]   # 자리에 숫자 넣어
        recur(cnt+1, i+1)      # 다음자리에 지금자리보다 큰 수 넣으러 가



# 1부터 자연수 n까지, 중복없이 m개 고른 수열 구하기
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
answer = [0 for _ in range(m)]

recur(0, 0)