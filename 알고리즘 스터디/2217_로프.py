import sys
sys.stdin = open('input.txt')

n = int(input())
# 무거운 중량을 버티는 로프를 쓰는것이 무조건 이득이므로 정렬해준다.
# 그래서 로프가 약한 것일수록 버리면서 무게를 구해보는 방식
ropes = sorted([int(input()) for _ in range(n)], reverse=True)

max_w = 0   # 들어올릴 수 있는 최대 중량

while ropes:
    w = ropes[-1] * n  # 현 조합에서 들어올릴 수 있는 최대 중량

    # 현재 로프의 조합이 예전 조합보다 더 많이 들어올릴 수 있다면 업뎃
    if max_w < w:
        max_w = w

    # 다음 계산을 위해 제일 가벼운 로프 제거
    ropes.pop()
    n -= 1

print(max_w)



