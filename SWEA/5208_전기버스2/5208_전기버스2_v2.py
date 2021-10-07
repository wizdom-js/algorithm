import sys
sys.stdin = open('sample_input.txt')


def recur(now, cnt):
    global answer

    if now == n-1:
        answer = min(answer, cnt)
        return

    if answer <= cnt:
        return

    for i in range(1, bus_stop[now] + 1):    # 현재위치의 배터리만큼 갈 수 있는 곳까지 가기
        recur(now+i, cnt+1)

for idx in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    n = temp[0]     # 정류장 수
    bus_stop = temp[1:]  # 정류장 별 배터리 용량

    answer = 999999999999
    recur(0, 0)

    print('#{} {}'.format(idx, answer-1))