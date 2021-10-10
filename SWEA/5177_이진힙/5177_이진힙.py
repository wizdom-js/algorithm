import sys
sys.stdin = open('sample_input.txt')


tc = int(input())

for idx in range(1, tc+1):
    n = int(input()) # 목표 노드
    node = [0] + list(map(int, input().split())) # 노드들 받아오기
    answer = 0

    # 위치 바꾸기
    for i in range(1, n+1):
        while node[i//2] > node[i]: # 부모가 나보다 클때 바꿔주기
            node[i//2], node[i] = node[i], node[i//2]
            i //= 2     # 다음 조상도 검토

    # 조상 노드 다 더하기
    p = n//2    # n의 부모부터 시작이니까
    while p > 0:
        answer += node[p]
        p //= 2
    print(node)
    print('#{} {}'.format(idx, answer))