import sys
sys.stdin = open('input.txt')

n = int(input())
weight = sorted(list(map(int, input().split())))    # 무게가 작은 추부터 사용하도록 정렬

total_w = 1 # 측정할 수 있는 곳까지의 무게를, 만들 수 있는 추들의 합 +1 -> 측정할 수 없는 무게의 최솟값
for w in weight:
    # 여태까지 더한 추들의 무게가 현재 추의 무게보다 작다면
    # total_w 까지의 무게만 표현할 수 있다.
    if total_w < w:
        break

    # 여태까지 더한 추들의 무게가 현재 추의 무게보다 크다면 갱신
    total_w += w

print(total_w)

