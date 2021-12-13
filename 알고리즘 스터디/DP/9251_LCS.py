import sys
sys.stdin = open('input.txt')

seq1 = input()
seq2 = input()
seq_l1 = len(seq1) + 1
seq_l2 = len(seq2) + 1
dp = [[0 for _ in range(seq_l2)] for _ in range(seq_l1)]

for i in range(1, seq_l1):
    for j in range(1, seq_l2):
        if seq1[i-1] == seq2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])