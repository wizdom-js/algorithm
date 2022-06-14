def DFS(n, com, visited, computers) :
    visited[com] = True
    
    for j in range(n) :
        if com != j and computers[com][j] == 1:
            if visited[j] == False :
                DFS(n, j, visited, computers)


def solution(n, computers):
    visited = [False for i in range(n)]
    answer = 0
    
    for com in range(n) :
        if visited[com] == False :
            DFS(n, com, visited, computers)
            answer += 1
            
    return answer