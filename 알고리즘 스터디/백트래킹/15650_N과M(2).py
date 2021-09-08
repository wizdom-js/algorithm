import sys
sys.stdin = open('input.txt')

# 인덱스, 시작 숫자
def recur(cur, s):
    # m개 다 골랐다면 print
    if cur == m:
        print(*arr)
        return

    for i in range(s, n+1):
        arr[cur] = i    # 리스트에 숫자 담기
        recur(cur+1, i+1)   # 다음 자리에 지금보다 큰 숫자부터 탐색


n, m = map(int, input().split()) # 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
arr = [0 for _ in range(m)] # 수열 담을 리스트
recur(0, 1)


