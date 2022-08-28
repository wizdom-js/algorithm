def solution(survey, choices):
    answer = ''
    char_type = {'R': 0, 'T': 0, 'F': 0, 'C': 0, 'M': 0, 'J': 0, 'A': 0, 'N': 0}
    for idx, question in enumerate(survey):
        if choices[idx] == 4:
            continue
        elif choices[idx] - 4 < 0:
            char_type[question[0]] += abs(choices[idx] - 4)
        else:  # right
            char_type[question[1]] += abs(choices[idx] - 4)

    if char_type['R'] >= char_type['T']:
        answer += 'R'
    else:
        answer += 'T'
    if char_type['C'] >= char_type['F']:
        answer += 'C'
    else:
        answer += 'F'
    if char_type['J'] >= char_type['M']:
        answer += 'J'
    else:
        answer += 'M'
    if char_type['A'] >= char_type['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer