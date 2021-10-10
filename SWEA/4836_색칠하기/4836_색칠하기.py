import sys
sys.stdin = open('input.txt')

# 색칠하기 함수
def painting(purple):
    # 색칠할 박스 받아오기 [행 시작, 열 시작, 행 끝, 열 끝, 색깔]
    box = list(map(int, input().split()))

    # 색 (1: 빨강, 2: 파랑)
    color = box[4]

    # 왼쪽 위 모서리 에서 오른쪽 아래 모서리까지 색칠
    for x in range(box[0], box[2] + 1):
        for y in range(box[1], box[3] + 1):
            # # 같은 색은 겹치지 못하게 예외처리한 코드 (같은 색은 겹치지 않는다는 조건 없을경우)
            # # 해당 블럭에 아무것도 색칠 안되어 있다면 색칠하기
            # if board[x][y] == 0:
            #     board[x][y] = color
            # # 해당 블럭에 다른 색이 색칠되어 있다면 보라색이 된다(3)
            # # (같은 색이 아니고, 보라색이 아님)
            # elif board[x][y] not in (color, 3):
            #     board[x][y] = 3
            #     purple += 1

            # 같은 색은 겹치지 않는다는 조건이 있으므로 위의 조건은 필요 없다.
            board[x][y] += color
            if board[x][y] == 3:
                  purple += 1

    return purple


tc = int(input())

for idx in range(1, tc+1):
    n = int(input())                        # 색칠할 박스의 개수
    board = [[0] * 10 for _ in range(10)]   # 색칠할 보드

    purple = 0
    # 주어진 박스 개수만큼 반복
    for i in range(n):
        # 색칠하기 함수를 불러와, 보라색 개수 업뎃
        purple = painting(purple)


    print('#{} {}'.format(idx, purple))
    # for i in range(10):
    #     print(*board[i])

