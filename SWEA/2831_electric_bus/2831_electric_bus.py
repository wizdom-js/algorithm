import sys
sys.stdin = open('input.txt')

# 노선 T
t = int(input())

# 노선 t만큼 반복
for idx in range(1, t + 1):
    # 정류장 수 k, 종점 n, 충전기 설치된 곳의 수 m
    k, n, m = map(int, input().split())
    # 충전기가 설치된 곳
    charger = list(map(int, input().split()))

    now = 0  # 현재 위치
    battery = k  # 배터리 상태
    next_c = 0  # 다음 충전기 설치 된 곳의 idx
    answer = 0  # 최소 충전 횟수

    # 목표지점 전까지 반복
    # 목표지점에서는 배터리 0이어도 상관 X이므로
    while now < n - 1:
        now += 1  # 위치 이동
        battery -= 1  # 배터리 감소

        # 만약 현재 지점이 충전기가 설치된 곳이라면
        if now in charger:

            # 다음 충전기 설치된 곳의 idx 변경
            if next_c != m:
                next_c += 1

            # 다음 충전기까지 배터리가 부족하다면,
            try:
                if charger[next_c] - now > battery:
                    battery = k
                    answer += 1

            # 또는 현재 충전기가 마지막인경우, 남은 거리가 남은 배터리보다 많다면 충전
            except:
                if next_c == m  and n - now > battery:
                    battery = k
                    answer += 1


        # print('now=', now, 'battery=', battery, 'answer=', answer, 'next_c=', next_c)

        # 목표 도달하지 못했는데 배터리가 없는 경우 0 반환하고 중단.
        if not battery:
            answer = 0
            break

    print('#{} {}'.format(idx, answer))