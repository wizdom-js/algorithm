import sys
sys.stdin = open('sample_input.txt')

########## 점화식 버전 아님 ###############

# 규칙 (입력 받은 숫자 n)
# n-20 * 2 + n - 10
# 맨 처음, 즉 n = 10일때부터 구해나가서, 입력받은 숫자 n까지 도달할때까지 구한다.
def paper_use(n):

    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        return 2 * paper_use(n-20) + paper_use(n-10)


t = int(input())

for t in range(1, t+1):
    n = int(input())
    print('#{} {}'.format(t, paper_use(n)))

