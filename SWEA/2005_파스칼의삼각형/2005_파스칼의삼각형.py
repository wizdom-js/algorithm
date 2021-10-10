import sys
sys.stdin = open('input.txt')

tc = int(input())

for idx in range(1, tc+1):

    n = int(input())    # 파스칼 삼각형의 크기
    temp = [1]          # 첫번째 줄

    # 2차원 리스트로 만들지 않고 바로바로 프린트 해주기 위해
    # 테스트케이스의 번호와 첫번째 줄을 먼저 프린트해준다.
    print('#{}'.format(idx))
    print(*temp)

    # 두번째 줄부터 시작하기 때문에 삼각형 크기-1(n-1)까지 반복
    for i in range(n-1):
        stack = [0] + temp + [0]    # 맨 처음과 끝에 있는 1은 더할게 없으니 현재의 위 라인의 양 끝에 0을 붙여준다.
        temp = []                   # 해당 라인의 숫자를 저장할 임시 리스트

        # 여기서 pop()은 맨 마지막 원소를 뽑는다.
        # 파스칼 삼각형은 뒤집어도 똑같으니 반대로 해도 상관 X 
        num_pop = stack.pop()       # 자신의 오른쪽 위 숫자 가져오기 (0)

        while stack:
            num_pop2 = stack.pop()              # 자신의 왼쪽 위 숫자 가져오기
            temp.append(num_pop + num_pop2)     # 자신의 왼쪽 위 숫자 오른쪽 위 숫자와를 더하여 temp에 저장한다.

            num_pop = num_pop2      # 자신의 오른쪽 숫자는 다음 자신의 왼쪽 숫자이므로 바꿔준다.

        # 해당 라인을 프린트 해준다.
        print(*temp)



