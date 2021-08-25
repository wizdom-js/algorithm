import sys
sys.stdin = open('input.txt')

tc = int(input())

for _ in range(tc):
    n = int(input())    # 방문할 상점의 수 n
    shops = sorted(list(map(int, input().split()))) # 상점의 위치
    answer = 0  # 차로 돌아오기 위해 걸어야 하는 거리의 최솟값

    # 주차 위치 (가운데에 해야 최솟값을 구할 수 있다.)
    parking_l = (shops[0] + shops[-1]) // 2
    # 상점들간 거리
    for i in range(n-1):
        answer += shops[i+1] - shops[i]

    answer += parking_l - shops[0]  # 주차한곳에서 맨 처음에 위치한 상점으로 이동한 거리
    answer += shops[-1] - parking_l # 쇼핑 다 하고 마지막 상점에서 주차한 곳으로 돌아온 거리

    print(answer)