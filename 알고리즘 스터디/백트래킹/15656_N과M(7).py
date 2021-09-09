import sys
sys.stdin = open('input.txt')

def recur(cnt):
    # 다골랐으면 출력해
    if cnt == m:
        print(*answer)
        return

    for i in range(n):
        answer[cnt] = arr[i] # 현재 자리에 숫자 넣어
        recur(cnt+1)    # 다음자리 숫자 찾으러가 (어떤 숫자든 상관 없음)


# n개의 자연수 중에서 m개를 고른 수열
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split()))) #오름차순이니 정렬
answer = [0 for _ in range(m)]

# recur(0)


for i in range(n):
    for cnt in range(m):
        answer[cnt] = arr[i]
