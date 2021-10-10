import sys
sys.stdin = open('sample_input.txt')


# 후위 순회 알고리즘 / 어떤 순회를 써도 상관 엑스
def postorder(n):
    global answer
    if n:
        postorder(left[n])
        postorder(right[n])
        answer += 1


tc = int(input())

for idx in range(1, tc+1):
    e, n = map(int, input().split())    # 간선의 개수 e, 시작 노드 n
    node = list(map(int, input().split()))  # 노드 연결 정보 받아오기

    left = [0 for _ in range(e+2)]  # 부모를 인덱스로 자식번호 저장
    right = [0 for _ in range(e+2)]

    for i in range(0, e*2, 2):
        p, c = node[i], node[i+1]   # 부모 자식 노드 가져오기
        if left[p]:      # p의 왼쪽 자식 있으면 오른쪽 자식으로 저장
            right[p] = c
        else:           # p의 왼쪽 자식 없으면 왼쪽에 저장
            left[p] = c

    answer = 0
    postorder(n)

    print('#{} {}'.format(idx, answer))
