def delete_blocks(m, n, board, cnt):
    del_blocks = [] # 지울 블록 담는 리스트
    # 4블록있는지 검사
    for i in range(m - 1):
        for j in range(n - 1):
            block = board[i][j]
            if block == 0:  # 없어진 block 이라면 pass
                continue
            # 4개의 같은 블록이 붙어있을 경우
            if block == board[i][j + 1] and block == board[i + 1][j] and block == board[i + 1][j + 1]:
                del_blocks.extend([[i, j], [i, j + 1], [i + 1, j], [i + 1, j + 1]]) # 리스트에 추가

    # 4블록 없애기
    if del_blocks:
        for i, j in del_blocks:
            if board[i][j]: # 해당 자리 블록 있다면 (중복방지)
                board[i][j] = 0 # 없애기
                cnt += 1        # count
        return cnt
    else:
        return False    # 더 이상 없앨 블록 없다면 False 반환


def solution(m, n, board):
    board = list(map(list, zip(*board)))    # 보드 뒤집기

    cnt = 0
    while True:
        temp = delete_blocks(n, m, board, 0)    # 4블록 지워줘요
        if temp:    # 만약 지울 블록 있었다면
            cnt += temp # 지운 블록만큼 더해주기
            for i in range(n):
                board[i].sort(key=lambda x: type(x) is int, reverse=True)   # 빈공간 채우기 (0 다 앞으로 밀어)
        else:
            return cnt  # 더이상 4블록 없다면 없어진 블록 총 개수 반환


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))