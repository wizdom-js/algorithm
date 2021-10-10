import sys
sys.stdin = open('s_input.txt')

t = int(input())

for idx in range(1, t+1):
    print('#{}'.format(idx), end=' ')
    # 버스 노선 n개
    n = int(input())

    # 버스 노선 받아오기
    bus_lines = []
    for _ in range(n):
        d, a = map(int, input().split())        # 출발 노선, 도착 노선
        bus_lines.append(list(range(d, a+1)))   # d이상, a 이하인 모든 정류장을 다니므로 해당 정류장을 리스트로 만들어 넣어준다.

    # 검토할 버스 정류장 p개
    p = int(input())

    for _ in range(p):
        c = int(input())    # 버스 정류장
        cnt = 0             # 버스 정류장을 지나는 버스 노선의 개수

        # 버스 정류장이 각 버스 노선에 들어가있다면 count
        for line in bus_lines:
            if c in line:
                cnt += 1
        print(cnt, end=' ')
    print()

