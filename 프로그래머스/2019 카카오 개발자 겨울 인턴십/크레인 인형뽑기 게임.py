def solution(board, moves):
    
    bucket = []
    answer = 0
    
    for i in range(len(moves)) :
        # 맨 윗줄이 0 이면 그 밑의 줄로 이동
        for j in range(len(board)) :
            item = board[j][moves[i]-1]
            if item != 0 :
                break
                
        # 한줄 전체가 비었을 경우 맨 처음으로 돌아감
        if item == 0 :
            continue
                    
        bucket.append(item)
        board[j][moves[i]-1] = 0
        if len(bucket) >= 2 and item == bucket[-2] :
            del bucket[-2:]
            answer += 2
    
    return answer