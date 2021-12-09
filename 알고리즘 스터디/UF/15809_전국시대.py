import sys
sys.stdin = open('input.txt')


# def find(x):
#     if parent[x] == x:
#         return x
#     parent[x] = find(parent[x])
#     return parent[x]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(o, x, y):
    x = find(x)
    y = find(y)

    if o == 1:
        parent[x] = y
        mp[y] += mp[x]
        return

    if mp[x] < mp[y]:
        parent[x] = y
        mp[y] -= mp[x]
    elif mp[y] < mp[x]:
        parent[y] = x
        mp[x] -= mp[y]
    else:
        parent[x] = 0
        parent[y] = 0


n, m = map(int, input().split())
mp = [0] + [int(input()) for _ in range(n)]
parent = list(range(n+1))

for _ in range(m):
    o, p, q = map(int, input().split())
    union(o, p, q)

for i in range(1, n+1):
    parent[i] = find(parent[i])

answer = []
for i in set(parent):
    if i == 0:
        continue
    answer.append(mp[i])

answer.sort()

print(len(answer))
print(*answer)

