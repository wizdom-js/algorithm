import sys
sys.stdin = open('sample_input.txt')


def recur(now, cnt, battery):
    global answer

    battery -= 1    # 배터리 감소

    if now == n-1:  # 마지막 정류장까지 온 경우
        answer = min(answer, cnt)   # 작은 횟수로 갱신
        return

    if answer <= cnt:   # 가지치기
        return

    recur(now+1, cnt+1, bus_stop[now])  # 배터리 교체하는 경우
    if battery: # 배터리가 있을 경우에만
        recur(now+1, cnt, battery)  # 배터리 교체하지 않는 경우


for idx in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    n = temp[0]     # 정류장 수
    bus_stop = temp[1:]  # 정류장 별 배터리 용량

    answer = 999999999999
    recur(1, 0, bus_stop[0])

    print('#{} {}'.format(idx, answer))