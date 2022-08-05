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
    def dfs(idx, user_idx):
        nonlocal check, answer, permutation
        if idx == len(banned_id):
            permutation.append(user_idx)
            answer += 1
            return
        
        for i in ban_candidate[idx]:
            if not check[i]:
                continue
            check[i] = False
            user_idx.append(i)
            dfs(idx+1, user_idx)
            check[i] = True
            if user_idx:
                user_idx = user_idx[]
            
    
    check = [1 for _ in range(len(user_id))]
    permutation = []
    dfs(0, [])
    print(permutation)
            
    
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])

def check(users,banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False # 현재 튜플 불일치
    
    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id,len(banned_id)))
    banned_Set = []

    for users in user_permutation:
        # 하나의 튜플과 비교 시작
        if not check(users, banned_id):
            continue # 다음 튜플 가져오기
        else:
            users = set(users)
            if users not in banned_Set:
                banned_Set.append(users)

    return len(banned_Set)