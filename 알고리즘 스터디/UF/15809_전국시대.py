import sys
sys.stdin = open('input.txt')


# def find(x):
#     if parent[x] == x:
#         return x
#     parent[x] = find(parent[x])
#     return parent[x]

# 부모 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 합치기
def union(o, x, y):
    x = find(x)
    y = find(y)

    if o == 1:  # 동맹일때
        parent[x] = y   # 아무곳에나 합치고
        mp[y] += mp[x]  # 병력도 합치기
        return

    # 전쟁일 때
    # 병력이 더 많은 나라에 붙이고, 병력 수치 빼주기
    if mp[x] < mp[y]:
        parent[x] = y
        mp[y] -= mp[x]
    elif mp[y] < mp[x]:
        parent[y] = x
        mp[x] -= mp[y]
    else:   # 두 나라의 병력이 같을 경우 멸망
        parent[x] = 0
        parent[y] = 0


n, m = map(int, input().split())    # n개의 국가, m개의 기록
mp = [0] + [int(input()) for _ in range(n)]     # 각 국가의 병력의 수
parent = list(range(n+1))   # 부모 찾기 리스트

for _ in range(m):
    o, p, q = map(int, input().split()) # 기록 받아오기
    union(o, p, q)  # 합쳐주기

# 모든 국가의 각 부모 찾아주기
# (정리해주는 느낌 (반영 안된 나라도 있으므로))
for i in range(1, n+1):
    parent[i] = find(parent[i])

answer = []
for i in set(parent):   # 중복 거르기
    if i == 0:  # 멸망한 나라 제외
        continue
    answer.append(mp[i])    # 남아있는 국가의 병력의 수 리스트에 넣어주기

answer.sort()   # 오름차순으로 정렬

print(len(answer))
print(*answer)

