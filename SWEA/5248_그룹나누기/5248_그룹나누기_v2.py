import sys
sys.stdin = open('sample_input.txt')


def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

def union(x, y):
    x = find(x)
    y = find(y)

    if rank[x] > rank[y]:
        par[y] = x
    elif rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        rank[x] += 1


T = int(input())

for k in range(1, T + 1):
    N, M = map(int, input().split())

    temp = list(map(int, input().split()))
    par = list(range(N + 1))
    rank = [0 for i in range(N + 1)]

    for i in range(0, len(temp), 2):
        union(temp[i], temp[i + 1])

    print('#{} {}'.format(k, len(set(par))-1))



