import sys
sys.stdin = open('input.txt')


def recur(cnt, n):
    global answer
    if cnt == n:    # n만큼 바꿔줬다면
        temp = ''.join(board)   # 문자열로 바꿔주기
        if answer < temp:   # answer에 저장되어있는 값보다 크다면 갱신
            answer = temp
        return

    for i in range(len_b):
        for j in range(i+1, len_b): # 현재 자리(i)의 다음자리부터 비교
            board[i], board[j] = board[j], board[i] # 바꾸기
            temp = ''.join(board)               # 문자열로 바꿔
            if visited.get((temp, cnt), 1):     # 중복 아니라면
                visited[(temp, cnt)] = 0        # visited에 저장
                recur(cnt+1, n)                 # 들어가기
            board[i], board[j] = board[j], board[i] # 원상복귀


for idx in range(1, int(input())+1):
    board, n = input().split()
    n = int(n)
    board = list(board)
    len_b = len(board)
    visited = {}            # 중복 방지 딕셔너리
    answer = '00000000'     # 정답 담는 변수 초기화

    recur(0, n)

    print('#{} {}'.format(idx, answer))

'''
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10

'''