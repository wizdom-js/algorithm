import sys
sys.stdin = open('sample_input.txt')

tc = int(input())

for idx in range(1, tc+1):
    e, n = map(int, input().split())    # 간선의 개수 e, 시작 노드 n
    temp = list(map(int, input().split()))  # 노드 연결 정보 받아오기

    node = [[] for _ in range(e+2)]   # 노드 연결 정보 정리
    for i in range(0, e*2, 2):
        node[temp[i]].append(temp[i+1])

    answer = 1
    stack = node[n] # dfs 풀이
    while stack:
        n = stack.pop()
        answer += 1
        for i in node[n]:
            stack.append(i)

    print('#{} {}'.format(idx, answer))


