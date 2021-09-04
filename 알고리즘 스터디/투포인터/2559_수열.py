import sys
sys.stdin = open('input.txt')

# 온도를 측정한 전체 날짜 수 n, 합을 구하기 위한 연속적인 날짜의 수 k
n, k = map(int, input().split())
temp = list(map(int, input().split()))

si = 0  # 구간 시작 인덱스
temp_sum = answer = sum(temp[:k])   # 처음 합 설정해주기

# 처음에 k전까지의 구간을 합으로 만들어줬으니 k부터 시작
for i in range(k, n):
    # 구간 이동 해서 합 구하기
    # 구간의 맨 처음 온도(temp[si])을 빼주고, 현재 들어오는? 온도(temp[i])를 더해주면 된다.
    temp_sum = temp_sum - temp[si] + temp[i]

    # 온도의 합이 더 크다면 갱신
    if answer < temp_sum:
        answer = temp_sum

    si += 1     # 시작 인덱스 한칸 옮겨주기 (구간이니까)

print(answer)