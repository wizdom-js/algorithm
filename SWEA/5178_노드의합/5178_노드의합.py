import sys
sys.stdin = open('sample_input.txt')


tc = int(input())
for idx in range(1, tc+1):
    n, m, l = map(int, input().split())  # 노드의 개수 n, 리프 노드의 개수 m, 값을 출력할 노드 번호 l
    node = [0 for _ in range(n+1)]

    for _ in range(m):
        leaf, num = map(int, input().split())
        node[leaf] = num

    if n % 2: # 노드의 개수가 홀수인경우 아래에서 자식노드 i, i+1을 더해서 부모노드에 넣어주니까
        n -= 1  # -1을 해줄 필요가 있다. (즉, i+1때문에)

    for i in range(n, 1, -2):
        try:    # 자식 노드 두개 더해서 부모 노드에 넣어준다.
            node[i//2] = node[i] + node[i + 1]
        except IndexError:
            node[i//2] = node[i]    # 노드 개수 짝수인 경우는 하나 남기 때문에 예외처리.

        if node[l]: # 출력할 노드 번호의 값을 찾았다면 멈춰
            break

    print('#{} {}'.format(idx, node[l]))

