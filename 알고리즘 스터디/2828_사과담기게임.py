import sys
sys.stdin = open('input.txt')

# 스크린 크기 n, 바구니 크기 m
n, m = map(int, input().split())
# 사과 개수
j = int(input())

move = 0                # 이동 거리
s = 1                   # 바구니 시작 지점
e = s + m -1            # 바구나 끝 지점
for a in range(j):
    next_s = int(input())  # 다음 사과 떨어지는 위치

    # 다음 사과 떨어지는 위치가 바구니보다 왼쪽에 있다면
    if next_s < s:
        e -= s - next_s
        move += s - next_s
        s = next_s

    # 다음 사과 떨어지는 위치가 바구니보다 오른쪽에 있다면
    elif e < next_s:
        s += next_s - e
        move += next_s - e
        e = next_s

print(move)