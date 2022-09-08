def solution(survey, choices):
    answer = ''
    char_score = {'R': 0, 'T': 0, 'F': 0, 'C': 0, 'M': 0, 'J': 0, 'A': 0, 'N': 0}
    for char, choice in zip(survey, choices):
        if choice == 4:
            continue
        elif choice - 4 < 0:  # 비동의쪽 고른 경우
            char_score[char[0]] -= choice - 4
        else:                       # 동의쪽
            char_score[char[1]] += choice - 4

    # 성격 유형 정하기
    if char_score['R'] >= char_score['T']:
        answer += 'R'
    else:
        answer += 'T'
    if char_score['C'] >= char_score['F']:
        answer += 'C'
    else:
        answer += 'F'
    if char_score['J'] >= char_score['M']:
        answer += 'J'
    else:
        answer += 'M'
    if char_score['A'] >= char_score['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer