from itertools import permutations
 
 
def match(user, banned_id):
    for i in range(len(user)):
        if len(user[i]) == len(banned_id[i]):
            for j in range(len(user[i])):
                if user[i][j] != banned_id[i][j]:
                    if banned_id[i][j] == '*':
                        continue
                    else:
                        return False
        else:
            return False
    return True
 
 
def solution(user_id, banned_id):
    answer = []
 
    for banned_user in permutations(user_id, len(banned_id)):
        if match(banned_user, banned_id):
            banned_user = set(banned_user)
            if banned_user not in answer:
                answer.append(banned_user)
 
 
    return len(answer)

def solution(user_id, banned_id):
    ban_candidate = [[] for _ in range(len(banned_id))]
    
    
    # 밴 아이디 적용되는거 등록
    for u in range(len(user_id)):
        u_id = user_id[u]
        for b in range(len(banned_id)):
            b_id = banned_id[b]
            len_b_id = len(b_id)
            
            # 밴 아이디와 유저 아이디 길이 다르면 패스 
            if len_b_id != len(u_id):
                continue
                
            for i in range(len_b_id):
                if b_id[i] != u_id[i] and b_id[i] != '*':
                    break
            else:
                ban_candidate[b].append(u)
    
    print(ban_candidate)
    
    answer = 0
    def dfs(idx):
        nonlocal check, answer
        if idx == len(user_id):
            print(check)
            if sum(check) == 0:
                answer += 1
            return
        
        for i in ban_candidate[idx]:
            if not check[i]:
                continue
            check[i] = False
            dfs(idx+1)
            check[i] = True
    
    check = [1 for _ in range(len(user_id))]
    dfs(0)
            
    return answer