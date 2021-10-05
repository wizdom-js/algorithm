import sys
sys.stdin = open('sample_input.txt')


for idx in range(1, int(input())+1):
    n = int(input())    # 신청서 n
    time = [tuple(map(int, input().split())) for _ in range(n)]

    # 작업 끝나는 시간을 기준으로 오름차순 정렬
    # 빨리 끝나는 작업을 앞으로 둬야 계산을 많이 해볼 수 있기 때문이다.
    time.sort(key=lambda x: x[1])

    answer = 0
    temp_e = 0  # 이전 작업의 종료 시간
    for s, e in time:
        if temp_e <= s: # 현 작업 시작 시간과 이전 작업의 종료 시간이 안겹치면
            answer += 1
            temp_e = e  # 갱신

    print('#{} {}'.format(idx, answer))