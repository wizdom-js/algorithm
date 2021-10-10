import sys
sys.stdin = open("input.txt")


######## 중위 표기법 + 후위 표기법 ############


# 중위 표기법 -> 후위 표기법 변환
def infix_to_postfix(expression):

    cal = ''  # 후위 표기법 받을 문자열
    stack = []  # 스택
    for e in expression:

        # e가 숫자라면 cal에 더하기
        if e not in '(*/+-)':
            cal += e

        # e가 연산자라면
        else:
            # e가 여는 괄호라면 stack에 push
            if e == '(':
                stack.append('(')

            # e가 '*' 또는 '/' 라면
            elif e in '*/':
                # 스택 top의 연산자의 우선순위가 e의 우선순위보다 작을 때까지
                # stack pop 하여 가져와서 cal에 더하기
                while stack and stack[-1] in '*/':
                    cal += stack.pop()
                # 이제 없다면 stack에 e를 push 한다.
                stack.append(e)

            # e가 '+' 또는 '-' 라면
            elif e in '+-':
                # 스택 top의 연산자의 우선순위가 e의 우선순위보다 작을 때까지('('나오기 전까지)
                # stack pop하고 cal에 더한다.
                while stack and stack[-1] != '(':
                    cal += stack.pop()
                # 이제 없다면 stack에 e push
                stack.append(e)

            # e가 닫는 괄호라면 stack에서 여는 괄호가 나올때까지 pop연산을 수행하고 더한다
            elif e == ')':
                while stack and stack[-1] != '(':
                    cal += stack.pop()
                stack.pop() # 여는 괄호 버리기

    # stack에 남아있는 연산자 cal에 더해주면 후위 표기식 완성
    while stack:
        cal += stack.pop()

    return cal


# 후위 표기법의 수식 계산
def cal_postfix(expression):
    stack = []
    for e in expression:
        # e가 숫자라면 stack에 push
        if e.isdigit():
            stack.append(int(e))

        # e가 연산자라면 stack에서 숫자 두개를 꺼내와 연산자로 계산 후 stack에 push
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if e == '+':
                stack.append(num2 + num1)
            elif e == '-':
                stack.append(num2 - num1)
            elif e == '*':
                stack.append(num2 * num1)
            elif e == '/':
                if (not num1) or (not num2):
                    stack.append(0)
                else:
                    stack.append(num2 // num1)

    return stack.pop()  # 최종 값 반환



for idx in range(1, 11):
    n = int(input())
    expression = input()    # 식 받아오기

    # 중위 표기법 -> 후위 표기법 변환
    postfix = infix_to_postfix(expression)

    # 후위 표기법의 수식 계산
    result = cal_postfix(postfix)

    print('#{} {}'.format(idx, result))