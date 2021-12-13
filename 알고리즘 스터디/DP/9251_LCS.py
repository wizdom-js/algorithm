import sys
sys.stdin = open('input.txt')

seq1 = input()  # 문자열 1
seq2 = input()  # 문자열 2
seq_l1 = len(seq1) + 1  # 1번 문자열의 길이
seq_l2 = len(seq2) + 1  # 2번 문자열의 길이
dp = [[0 for _ in range(seq_l2)] for _ in range(seq_l1)]

for i in range(1, seq_l1):  # dp 배열 행열에 맞춰서(seq1-행, seq2-열) for문 선언
    for j in range(1, seq_l2):
        if seq1[i-1] == seq2[j-1]:  # 가장 최근에 추가된 글자가 같다면
            dp[i][j] = dp[i-1][j-1] + 1 # 글자가 추가되기 전, 최대 길이 + 1
        else:   # 다르다면
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])  # 기존에 주어진 문자열로 만들 수 있었던 길이 중, 최대 길이 선택

print(dp[-1][-1])