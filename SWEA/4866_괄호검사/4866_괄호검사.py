import sys
sys.stdin = open('sample_input.txt')

# 괄호의 짝을 찾기 위해 딕셔너리 활용
b_dict = {'(':')', '{':'}', '[':']'}

t = int(input())

for idx in range(1, t+1):
    code = input()
    stack = []
    answer = 0

    for c in code:
        # c가 여는 괄호 중 하나라면 stack에 추가
        if c in b_dict.keys():
            stack.append(c)

        # c가 닫는 괄호 중 하나라면
        elif c in b_dict.values():
            # stack이 비어있지 않다면 stack에서 괄호 빼오기
            try:
                pop_b = stack.pop()
                # 만약 pop한 여는 괄호가 c(현재 닫는 괄호)와 짝이 아니라면 아예 답이 틀린거 -> 중단
                if b_dict[pop_b] != c:
                    break
            # stack이 비어있다면
            except:
                break

    # 위에서 틀린경우 없었다면
    else:
        # 근데 여는 괄호랑 닫는 괄호랑 짝이 다 맞아서 stack이 비워졌다면
        if not stack:
            answer = 1

    print('#{} {}'.format(idx, answer))
