import sys
sys.stdin = open('input.txt')

# 10개의 테스트 케이스
for idx in range(1, 11):
    # 빌 개수
    n = int(input())
    # 빌딩 정보 받아오기
    buildings = list(map(int, input().split()))

    # 조망권 확보한 세대 수
    view  = 0
    # 양 끝의 0빼고 빌딩 돌기
    for i in range(2, n-2):
        # 빌딩 없는 곳은 생략한다.
        if buildings[i] == 0:
            continue

        # 왼쪽 두칸과 오른쪽 두칸이 현재 건물보다 높지 않은지 판별하기
        # (하나라도 높은 경우에는 조망권 확보 아예 안됨)
        if buildings[i-2] < buildings[i] and buildings[i-1] < buildings[i] and buildings[i+1] < buildings[i] and buildings[i+2] < buildings[i]:
            # 양 옆의 건물들 중, 가장 높은 건물을 구하고,
            highest = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
            # 현재 건물의 높이에서 빼주면 조망권을 확보한 세대수가 나온다.
            view += (buildings[i]-highest)

    print('#{} {}'.format(idx, view))