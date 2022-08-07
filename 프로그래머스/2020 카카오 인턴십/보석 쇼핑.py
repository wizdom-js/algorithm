def solution(gems):
    n = len(gems)
    gem_kinds = len(set(gems))
    
    dic = {gems[0]:1}
    l, r = 0, 0
    
    answer = [1, n]
    while n > l :
        if len(dic) != gem_kinds :
            r += 1
            if r >= n :
                break
            
            if gems[r] in dic :
                dic[gems[r]] += 1
            else :
                dic[gems[r]] = 1
                
        else :
            if r - l < answer[1] - answer[0]:
                print('d')
                print(r, l, answer[1], answer[0])
                answer = [l+1, r+1]
                
            if dic[gems[l]] != 1 :
                dic[gems[l]] -= 1
            else :
                del dic[gems[l]] 
                
            l += 1
                
    return answer