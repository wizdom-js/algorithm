import sys
sys.stdin = open('input.txt')

n = int(input())
area = 100 * n      # 색종이 개수만큼 일단 크기 설정

board = [[0 for _ in range(101)] for _ in range(101)]   # 흰 도화지 만들기

for i in range(n):
    # 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리 lx
    # 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리 by
    lx, by = map(int, input().split())

    # 입력받은 현재 색종이의 크기만큼 반복문을 돈다.
    for y in range(by, by+10):
        for x in range(lx, lx+10):
            # 만약 해당 자리에 이전 색종이가 있었다면 크기에서 -1해준다.
            if board[y][x]:
                area -= 1

            board[y][x] += 1    # 색종이 들어간다 표시

print(area)

# for i in range(26):
#     print(*board[i])
