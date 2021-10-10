import sys
sys.stdin = open('input.txt')

# 중위 순회
def in_order(n):
    if n:
        in_order(left[n])
        print(tree[n], end='')  # 정점의 알파벳 출력
        in_order(right[n])


for idx in range(1, 11):
    n = int(input())

    tree = [0 for _ in range(n+1)]      # 트리(알파벳)
    left = [0 for _ in range(n+1)]      # 왼쪽 자식 받을거야
    right = [0 for _ in range(n+1)]     # 오른쪽 자식 받을거야

    # 정점 정보를 받아올 때, 맨앞에 정점번호 int로 바꿔주기 귀찮으니 i로 한다. (1부터 n까지의 정수라고 주어짐)
    for i in range(1, n+1):
        info = input().split()  # 정점 정보 받기
        tree[i] = info[1]       # 트리에 알파벳 넣기

        # 자식이 없는 경우는 index 에러가 나니 try except로 해준다.
        try:
            left[i] = int(info[2])      # 왼쪽 자식
            right[i] = int(info[3])     # 오른쪽 자식
        except IndexError:
            continue

    print('#{}'.format(idx), end=' ')
    in_order(1)
    print()