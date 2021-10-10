import sys
sys.stdin = open("sample_input.txt")

tc = int(input())

for idx in range(1, tc+1):
    expression = list(input().split())

    stack = []
    result = 'error'    # 결과 저장 변수
    for e in expression:

        # e가 숫자일 경우 stack에 push. 나중 연산 편하게 하기 위해 int로 변환
        if e.isdigit():
            stack.append(int(e))

        # e가 숫자 아닐 경우. 그리고 stack에 뽑을 숫자 있을 경우.
        elif stack:
            # 숫자 하나 뽑는다
            num1 = stack.pop()
            # e가 연산자일 경우
            if e in '*/+-' and stack:
                # 숫자 하나 더 뽑아와서 e에 해당하는 연산자에 맞게 계산 후 stack에 push
                num2 = stack.pop()
                if e == '*':
                    stack.append(num2 * num1)
                elif e == '/':
                    stack.append(num2 // num1)  # 나눈 값이 정수여야하니 // 연산자로 몫만 가져오기
                elif e == '+':
                    stack.append(num2 + num1)
                elif e == '-':
                    stack.append(num2 - num1)

            # e가 .일 경우.
            # 이미 위에서 숫자 하나 뽑았으니 stack에 더이상 남아있는 값이 없을 경우
            elif e == '.':
                if not stack:
                    result = num1

    print('#{} {}'.format(idx, result))


