import sys
sys.stdin = open('input.txt')

for idx in range(1, 11):
    n, string = map(str, input().split())

    stack = []
    for s in string:
        # stack이 비어있지 않고, stack의 마지막 글자와 s와 같다면 중복이므로 pop으로 삭제
        if stack and s == stack[-1]:
            stack.pop()
        # 중복이 아니라면 추가 
        else:
            stack.append(s)

    print('#{} {}'.format(idx, ''.join(stack)))