import sys
sys.stdin = open('input.txt')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    parent[x] = y

# 각 이름의 parent리스트의 인덱스 구하기
def nameIdx(name):
    global dic_idx
    if name not in name_dic:
        name_dic[name] = dic_idx
        name_idx = dic_idx
        dic_idx += 1
    else:
        name_idx = name_dic[name]

    return name_idx

test_n = 0  # 테스트 케이스 번호
while True:
    test_n += 1
    n = int(input())
    if not n: break # 입력의 끝일 경우

    parent = list(range(n+1))   # 고리 찾기(부모찾기) 리스트
    name_dic = dict()   # 이름 : parent 리스트의 인덱스
    dic_idx = 0 # parent 리스트의 인덱스

    for _ in range(n):
        name1, name2 = input().split()

        # 각 이름의 인덱스 구하기
        name1_idx = nameIdx(name1)
        name2_idx = nameIdx(name2)

        # 합치기
        union(name1_idx, name2_idx)

    # 정리해주기 (각 부모 찾아주기)(부모 => 처음 마니또 베품 받은 사람)
    for i in range(n):
        parent[i] = find(parent[i])

    print(test_n, len(set(parent))-1)
