import sys
sys.stdin = open('input.txt')


# 입력 받기
n1, n2 = map(int, input().split())
tmp_ants1 = input()
tmp_ants2 = input()
t = int(input())

# 첫 번째 그룹 개미가 두 번째 그룹 개미 다 뛰어넘은 경우
if n1 + n2 - 1 <= t:
    print(tmp_ants2 + ''.join(reversed(tmp_ants1)))
    exit()

# 개미들 넣을 리스트 만들어주기
# 두칸씩 띄워 넣을 것이기 때문에 넉넉하게 만들기
sum_ants = [0 for _ in range((n1 + n2) * 3)]
tt = t*2

# 첫 번째 그룹 개미들 넣기
idx = n1 - 1    # 반대 방향이므로 뒤집어서 넣기
for i in range(tt, tt + n1*2, 2):
    sum_ants[i] = tmp_ants1[idx]
    idx -= 1

# 두 번째 그룹 개미들 넣기
idx = 0
for j in range(i - tt, i - tt + n2*2, 2):
    sum_ants[j+1] = tmp_ants2[idx]
    idx += 1

# 개미들 이어주기
answer = ''
for ant in sum_ants:
    if ant:
        answer += ant

print(answer)