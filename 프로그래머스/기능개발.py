from collections import deque

def solution(progresses, speeds):
    days = deque()
    
    for per, speed in zip(progresses, speeds) :
        day = -((per - 100)// speed)
        days.append(day)
    
    count = 1
    answer = []
    for i in range(1, len(days)) :
        if days[i] <= days[i-1] :
            days[i] = days[i-1]
            count += 1
        else :
            answer.append(count)
            count = 1
            
        if i == (len(days)-1) :
            answer.append(count)
            
    return answer