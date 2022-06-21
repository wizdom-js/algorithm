def solution(people, limit):
    people.sort()
    boat = 0
    
    r = len(people) -1
    l = 0
    
    while l <= r :
        if people[l] + people[r] <= limit :
            l += 1
            
        r -= 1
        boat += 1
        
    return boat