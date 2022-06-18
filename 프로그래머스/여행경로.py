def solution(tickets):
    
    path = {}
    
    for (start, end) in tickets:
        path[start] = path.get(start, []) + [end]
    
    for r in path.keys():
        path[r].sort(reverse=True)

    answer = []       
        
    stack = ["ICN"]  
    while stack :
        now = stack[-1]
        if now not in path or len(path[now]) == 0 :
            answer.append(stack.pop())
        else :
            stack.append(path[now][-1])
            path[now] = path[now][:-1]

    return answer[::-1]