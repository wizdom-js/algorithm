def solution(s):
    temp = []
    for word in s:
        if temp and temp[-1] == word:
            temp.pop()
        else:
            temp.append(word)
    
    return 0 if temp else 1