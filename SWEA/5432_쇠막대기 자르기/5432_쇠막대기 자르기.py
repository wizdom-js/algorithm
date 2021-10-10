import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for idx in range(1, t+1):
    iron_bar = list(input())[::-1]  # pop사용할건데 걍 편하게 생각하기 위해 뒤집어줌.
    temp_bar = 0        # 쇠막대기가 생기면 count
    total_bar = 0       # 총 쇠막대기 개수

    b1 = iron_bar.pop()         # 괄호 받아오기
    while iron_bar:
        b2 = iron_bar.pop()     # 괄호 받아오기

        # 만약 받아온 괄호 두개가 '()'으로 레이저라면
        if (b1, b2) == ('(', ')'):
            total_bar += temp_bar   # 생성된 막대기들만큼 조각나니까 총 쇠막대기 개수에 더해주기
            b1 = iron_bar.pop()     # 레이저의 다음 괄호로 넘어간다.

        # 레이저 아니라면
        else:
            # '(' == 막대기 시작(생김)
            if b1 == '(':
                temp_bar += 1    # 쇠막대기 생긴거니까 count

            # ')' == 막대기 끝남
            else:
                total_bar += 1   # 끝난 부분 막대기 count해주기
                temp_bar -= 1    # 남아있는 막대기에서 빼주기

            b1 = b2     # 다음괄호를 현재괄호로 바꿔준다.

    # 총 막대기에서 남아있는 막대기들 더해준다.
    pint('#{} {}'.format(idx, total_bar+temp_bar))


