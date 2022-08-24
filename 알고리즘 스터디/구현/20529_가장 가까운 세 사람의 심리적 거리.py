import sys
sys.stdin = open('input.txt')

def cal_score(mbti1, mbti2):
    score = 0
    for m1, m2 in zip(mbti1, mbti2):
        if m1 != m2:
            score += 1
    return score

def standard(mbti):
    score = [0, 0, 0, 0]
    for m in mbti:
        if m[0] == 'E':
            score[0] += 1
        else:
            score[1] -= 1

        if m[1] == 'N':
            score[1] += 1
        else:
            score[1] -= 1

        if m[2] == 'T':
            score[2] += 1
        else:
            score[2] -= 1

        if m[3] == 'J':
            score[3] += 1
        else:
            score[3] -= 1





tc = int(input())
for _ in range(tc):
    n = int(input())
    mbti = list(input().split())

    if n > 32:
        print(0)
    else:
        answer = 999999999999
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    tmp_score = 0
                    for z in range(4):
                        if mbti[i][z] != mbti[j][z]: tmp_score += 1
                        if mbti[j][z] != mbti[k][z]: tmp_score += 1
                        if mbti[i][z] != mbti[k][z]: tmp_score += 1

                    answer = min(tmp_score, answer)

        print(answer)



