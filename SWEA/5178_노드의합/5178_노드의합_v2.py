import sys
sys.stdin = open('sample_input.txt')


tc = int(input())
for idx in range(1, tc+1):
    n, m, l = map(int, input().split())  # 노드의 개수 n, 리프 노드의 개수 m, 값을 출력할 노드 번호 l
    node = [0 for _ in range(n+2)]  # n이 짝수인 경우, 노드 개수가 하나 남기 때문에 아래에서 인덱스 에러를 막기 위해 넉넉하게 하나 더 만들어줌

    # 리프 노드 데이터 삽입
    for _ in range(m):
        leaf, num = map(int, input().split())
        node[leaf] = num

    # 값이 비어있는 노드부터 거꾸로 올라감
    for i in range(n-m, 0, -1):
        node[i] = node[i*2] + node[i*2+1]   # 부모노드 i에 자식노드 두개 더해 넣어주기

    print('#{} {}'.format(idx, node[l]))

