import sys
sys.stdin = open('input.txt')


def recur(cnt):
    # m개 다 골랐다면 print
    if cnt == m:
        print(*arr)
        return

    for i in range(1, n+1):
        arr[cnt] = i    # 리스트에 숫자 넣기
        recur(cnt+1)    # 다음 자리에 들어가서 가져와


# 1부터 자연수 n까지, m개 고른 수열 구하기
n, m = map(int, input().split())
arr = [0 for _ in range(m)] # 수열담는 리스트

recur(0)

