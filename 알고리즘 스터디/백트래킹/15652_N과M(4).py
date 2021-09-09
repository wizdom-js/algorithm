import sys
sys.stdin = open('input.txt')

def recur(cnt, s):
    if cnt == m:
        print(*arr)
        return

    for i in range(s, n+1):
        arr[cnt] = i    # 지금 자리에 숫자 넣어
        recur(cnt+1, i) # 다음자리에 넣을 숫자 가지고 와도 되는데 지금 숫자부터 시작해봐


# 1부터 자연수 n까지, m개 고른 수열 구하기
n, m = map(int, input().split())
arr = [0 for _ in range(m)]

recur(0, 1)
