import sys
sys.stdin = open('input.txt')


def find(std):
    if root[std] != std:
        root[std] = find(root[std])
    return root[std]

def union(std1, std2):
    std1 = find(std1)
    std2 = find(std2)

    if friend_fee[std1-1] < friend_fee[std2-1]:
        root[std2] = std1
    elif friend_fee[std2-1] < friend_fee[std1-1]:
        root[std1] = std2
    else:
        root[std2] = std1


n, m, k = map(int, input().split()) # 학생 수 n, 친구관계 수 m, 가지고 있는 돈 k
friend_fee = list(map(int, input().split()))

root = list(range(n+1))
for _ in range(m):
    student1, student2 = map(int, input().split())
    union(student1, student2)


for i in range(1, n+1):
    root[i] = find(root[i])

answer = 0
for std_idx in set(root[1:]):
    answer += friend_fee[std_idx - 1]
    if k < answer:
        print('Oh no')
        exit()
print(answer)