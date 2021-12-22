import sys
sys.stdin = open('input.txt')

seq1 = input()
seq2 = input()
seq1_l = len(seq1) + 1
seq2_l = len(seq2) + 1
dp = [["" for _ in range(seq2_l)] for _ in range(seq1_l)]

for i in range(1, seq1_l):
    for j in range(1, seq2_l):
        if seq1[i-1] == seq2[j-1]:
            dp[i][j] = dp[i-1][j-1] + seq1[i-1]
        else:
            if len(dp[i-1][j]) < len(dp[i][j-1]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

lcs_l = len(dp[-1][-1])
print(lcs_l)
if lcs_l:
    print(dp[-1][-1])


'''
CAPCAK
ACAYKP
'''