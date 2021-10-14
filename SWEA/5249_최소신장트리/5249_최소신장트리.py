import sys
sys.stdin = open('sample_input.txt')


########### Kruskal ###########

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


tc = int(input())
for idx in range(1, tc+1):
    v, e = map(int, input().split())
    par = list(range(v+1))  # 루트
    rank = [0 for _ in range(v+1)]

    tmp = []
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        tmp.append([n1, n2, w])
    tmp.sort(key=lambda x: x[2])    # 가중치에 따라 오름차순으로 정렬 -> 가중치가 가장 낮은 간선부터 선택하면서 트리 증가

    answer = 0
    for arr in tmp:
        if find(arr[0]) == find(arr[1]):    # 사이클이 존재(이미 연결되어 있으면)하면 다음으로 가중치가 낮은 간선 선택
            continue
        union(arr[0], arr[1])
        answer += arr[2]

    print('#{} {}'.format(idx, answer))