import sys
sys.stdin = open('input.txt')

# find(root 찾기) 
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

# union(x, y 연결)
def union(x, y):
    x = find(x)
    y = find(y)
    root[x] = y


n = int(input())    # 도시의 수
m = int(input())    # 여행 계획에 속한 도시의 수

connected_info = [list(map(int, input().split())) for _ in range(n)]    # 도시의 연결 정보 
plan = list(map(int, input().split()))  # 여행 계획 

root = list(range(n))   # 각 도시의 루트를 저장할 리스트

for i in range(n):
    for j in range(n):
        if connected_info[i][j]:    # 연결되어 있는 곳이라면 
            union(i, j) # 합치기 

result = set([find(p-1) for p in plan]) # 여행 계획지들의 루트 정리 
if len(result) == 1:    # 루트가 1개라면 
    print('YES')
else:   # 2개 이상이라면 이어져있지 않음 
    print('NO')

# root_n = -1
# for p in plan:
#     root[p-1] = find(root[p-1])
#     if root_n == -1:
#         root_n = root[p-1]
#     else:
#         if root_n != root[p-1]:
#             print('NO')
#             exit()
#         else:
#             print('YES')
#             exit()