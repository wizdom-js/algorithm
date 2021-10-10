import sys
sys.stdin = open('sample_input.txt')

def bfs(s, g):
    q = [s]          # 큐 생성 및 시작점 넣어주기
    while q:
        now = q.pop(0)  # 큐의 맨 앞에서 저장된 노드 가져오기

        if now == g:    # 현재 노드가 목표 노드라면 중지
            return

        for i in adj[now]:      # 현재 노드에서 연결된 노드 다가져와
            if not distance[i]: # 연결된 노드 i가 아직 방문 안한곳이면
                q.append(i)     # 방문해봐야지. q에 넣어준다.

                # 출발노드 ~ 노드 i 까지의 거리 =  출발노드 ~ 현재노드까지의 거리 +1
                # 왜냐면 현재 노드(변수 now)에서 1칸 움직인거니까
                distance[i] = distance[now] + 1


tc = int(input())
for idx in range(1, tc+1):
    v, e = map(int, input().split())    # 노드 개수 v, 연결 정보 개수 e

    # 인접리스트 생성
    adj = [[] for _ in range(v+1)]
    for _ in range(e):
        s, e = map(int, input().split())    # 간선의 양쪽 노드 번호 s, e
        adj[s].append(e)
        adj[e].append(s)

    s, g = map(int, input().split())    # 출발 노드 s, 도착 노드 g
    distance = [0] * (v+1)   # 출발점부터의 거리 저장할 리스트 (인덱스 편하게 사용 하기 위해 v+1)

    bfs(s, g)

    print('#{} {}'.format(idx, distance[g]))


