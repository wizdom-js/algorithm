import sys
sys.stdin = open('sample_input.txt')


def make_tree(node):
    global cnt

    if node <= n:
        make_tree(node*2)   # 왼쪽 노드
        tree[node] = cnt    # 왼쪽 다 다녀 왔으면 값 넣어
        cnt += 1
        make_tree(node*2+1) # 오른쪽 노드


tc = int(input())

for idx in range(1, tc+1):
    n = int(input()) # 이진 탐색 트리에 저장할 노드 개수

    tree = [0 for _ in range(n+1)]

    cnt = 1
    make_tree(1)    # 중위순회 하면 오름차순으로 정렬된 값을 얻을 수 있다.

    print('#{} {} {}'.format(idx, tree[1], tree[n//2]))

