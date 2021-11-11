import sys
sys.stdin = open('input.txt')

# " 어떤 대학교에서든 모든 대학교로 이동이 가능한 경로" => UF
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    # 깊이가 더 깊은 곳에 붙인다.
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1


n, m = map(int, input().split())    # 학교의 수 n, 학교를 연결하는 도로의 개수 m
uni = list(input().split())         # 대학교 성별 정보

parent = list(range(n+1))           # root
rank = [0 for _ in range(n+1)]      # rank

arr = [[] for _ in range(m)]
for i in range(m):
    u, v, d = map(int, input().split()) # 연결되는 학교 u, v 거리 d
    arr[i] = [u, v, d]

arr.sort(key=lambda x: x[2])    # 경로 길이 최단거리가 되어야 한다고 했으므로 Kruskal => 거리 짧은 순으로 정렬
answer = 0
cnt = 0
for u, v, d in arr:
    if find(u) == find(v) or uni[u-1] == uni[v-1]:  # 사이클이 존재(이미 연결되어 있으면)하거나, 대학교 성별 같으면 패스
        continue
    union(u, v)     # 합치기
    # print(u, v, d)
    answer += d     # 거리 합치기
    cnt += 1        # 이어진 노드 개수 세기
    if cnt == n-1:  # 모든 노드 이어졌다면
        print(answer)   # 경로 길이 출력
        exit()

if cnt != n-1:  # 모든 학교를 연결하는 경로 없다면
    print(-1)   # -1 출력

# print(parent)
# print(rank)

'''
3 2
M W W
1 2 12
2 3 10

'''