def solution(skill, skill_trees):
    answer = 0
    
    skill_l = len(skill)
    for skill_tree in skill_trees:
        skill_p = 0
        for t in skill_tree:
            if t == skill[skill_p]:
                skill_p += 1
            else:
                if t in skill:
                    break
        else:
            answer += 1
                    
    return answer