import sys
sys.stdin = open('input.txt')

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        root[y] = x
    else:
        root[x] = y

n = int(input())    # 컴퓨터의 수
m = int(input())    # 연결할 수 있는 선의 수

root = list(range(n+1)) # 부모 노드를 기록할 리스트

tmp = []
for _ in range(m):
    computer1, computer2, cost = map(int, input().split())
    tmp.append([computer1, computer2, cost])

# 모든 컴퓨터를 연결하는데 드는 최소비용 => MST => 크루스칼 사용
tmp.sort(key=lambda x: x[2])    # 가중치에 따라 오름차순 정렬 -> 가중치가 가장 낮은 간선부터 선택하면서 트리 증가

answer = 0
# 연결하기
for line in tmp:
    if find(line[0]) == find(line[1]):  # 사이클이 존재(이미 연결되어 있으면)하면 다음으로 가중치가 낮은 간선 선택
        continue
    union(line[0], line[1])
    answer += line[2]

print(answer)


