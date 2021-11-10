import sys
sys.stdin = open('input.txt')


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


n, m = map(int, input().split())    # 학교의 수 n, 학교를 연결하는 도로의 개수 m
uni = list(input().split())

parent = list(range(n+1))
rank = [0 for _ in range(n+1)]

arr = [[] for _ in range(m)]
for i in range(m):
    u, v, d = map(int, input().split()) # 연결되는 학교 u, v 거리 d
    arr[i] = [u, v, d]

arr.sort(key=lambda x: x[2])
answer = 0
cnt = 0
for u, v, d in arr:
    if find(u) == find(v) or uni[u-1] == uni[v-1]:
        continue
    union(u, v)
    # print(u, v, d)
    answer += d
    cnt += 1
    if cnt == n-1:
        print(answer)
        exit()

if cnt != n-1:
    print(-1)

print(parent)
print(rank)

'''
3 2
M W W
1 2 12
2 3 10

'''