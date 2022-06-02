def solution(lottos, win_nums):
    count_z = lottos.count(0)
    lottos = sorted(lottos, reverse=True)
    answer = 0
    
    for num in lottos :
        if num == 0 :
            break
        elif num in win_nums :
            answer += 1
            
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    
    return [rank[answer+count_z], rank[answer]]