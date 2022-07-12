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

root = list(range(n+1))

tmp = []
for _ in range(m):
    computer1, computer2, cost = map(int, input().split())
    tmp.append([computer1, computer2, cost])

tmp.sort(key=lambda x: x[2])

answer = 0
for line in tmp:
    if find(line[0]) == find(line[1]):
        continue
    union(line[0], line[1])
    answer += line[2]

print(answer)


