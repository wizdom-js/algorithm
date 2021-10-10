import sys
sys.stdin = open('input.txt')

# 받은 행렬 90도 돌려주는 함수
def revolution_90(matrix):
    # 빈 행렬 만들기
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # 90도 돌리기
    for i in range(n):
        for j in range(n):
            new_matrix[j][n-i-1] = matrix[i][j]

    # ['1', '2', '3'] 이면 '123' 의 형태로 출력해야하기 때문에 붙여서 넣어주었다.
    complete = [''.join(line) for line in new_matrix]

    return complete


t = int(input())

for idx in range(1, t+1):
    print('#{}'.format(idx))
    n = int(input())

    # 행렬 받아오기
    matrix = []
    for _ in range(n):
        matrix.append(list(map(str, input().split())))

    d_90 = revolution_90(matrix)    # 받아온 행렬에서 90도 돌리기
    d_180 = revolution_90(d_90)     # 90도 돌린 행렬에서 90도 돌리기 -> 180도
    d_270 = revolution_90(d_180)    # 180도 돌린 행렬에서 90도 돌리기 -> 270도

    for i in range(n):
        # 90도, 180도, 270도의 i행 출력
        print(d_90[i], d_180[i], d_270[i])
