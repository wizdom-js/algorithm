import sys
sys.stdin = open('input.txt')

# "모든 행성 연결" => UF
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1


n = int(input())    # 행성의 수
parent = list(range(n+1))           # root
rank = [0 for _ in range(n+1)]

arr = []
for i in range(n):
    temp = list(map(int, input().split()))  # 관리비용
    for j in range(i+1, n):     # 양방향이므로
        arr.append((i, j, temp[j])) # 행성 i -> j, 관리비용  temp[j]

arr.sort(key=lambda x: x[2])    # 유지비용 최소화 하자고 했으므로 Kruskal => 유지비용 짧은 순으로 정렬
answer = 0
for p1, p2, d in arr:
    if find(p1) == find(p2):
        continue
    union(p1, p2)
    answer += d

print(answer)