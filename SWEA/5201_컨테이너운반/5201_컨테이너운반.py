import sys
sys.stdin = open('sample_input.txt')


tc = int(input())
for idx in range(1, tc+1):
    n, m = map(int, input().split())    # 컨테이너 수 n, 트럭 수 m

    # 트럭당 한 개의 컨테이너를 운반 할 수 있으니 각 트럭에 최대한 무거운 화물을 싣도록 한다.
    weight = sorted(list(map(int, input().split())), reverse=True)  # 화물의 무게
    trucks = sorted(list(map(int, input().split())))                # 트럭의 적재 용량

    total_w = 0
    t = trucks.pop()    # 큰 트럭 가져와
    for w in weight:    # 화물 무거운 것부터 탐색
        if w <= t:      # 화물 트럭에 실을 수 있다면
            total_w += w    # 화물 전체 무게에 더해주기
            if trucks:
                t = trucks.pop()    # 다음 트럭 오세요
            else:
                break               # 트럭 없다면 중단

    print('#{} {}'.format(idx, total_w))

