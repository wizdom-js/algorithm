from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for i in range(1, col+1) :
        candidates.extend(combinations(range(col), i))
    print(candidates)

    unique = []
    for candi in candidates :
        tmp = [tuple([item[i] for i in candi]) for item in relation]
        if len(set(tmp)) == row :
            unique.append(candi)

    answer = set(unique)
    for i in range(len(unique)) :
        for j in range(i+1, len(unique)) :
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])) :
                   answer.discard(unique[j])
    return len(answer)