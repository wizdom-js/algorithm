import sys
sys.stdin = open('input.txt')

seq1 = input()  # 문자열 1
seq2 = input()  # 문자열 2
seq1_l = len(seq1) + 1  # 각 문자열의 길이
seq2_l = len(seq2) + 1
dp = [["" for _ in range(seq2_l)] for _ in range(seq1_l)]   # LCS를 저장할 DP

for i in range(1, seq1_l):
    for j in range(1, seq2_l):
        if seq1[i-1] == seq2[j-1]:  # 방금 막 추가한 문자가 같다면
            dp[i][j] = dp[i-1][j-1] + seq1[i-1] # 기존 문자열 + 방금 문자
        else:                       # 같지 않다면
            if len(dp[i-1][j]) < len(dp[i][j-1]):   # 현재 dp의 좌측과 위의 값중에 더 큰 값으로 저장
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

lcs_l = len(dp[-1][-1]) # 두 문자열 LCS의 길이
print(lcs_l)
if lcs_l:   # LCS의 길이가 1 이상인 경우만 LCS 출력
    print(dp[-1][-1])


'''
CAPCAK
ACAYKP
'''