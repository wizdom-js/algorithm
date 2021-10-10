import sys
sys.stdin = open('sample_input.txt')

# 다시 확인하기
############# 점화식 버전 ###############

# 규칙 (입력 받은 숫자 n)
# 2 * (n-2) + (n-1)

# 점화식을 이용하기 위해 n의 크기마다 경우의 수를 저장할 리스트 만들기
# 규칙이 (현재의 수-2) * 2 + (현재의 수-1) 이므로 숫자 2개 필요
# n = 10일 경우 -> 1개 , n = 20일경우 -> 3개 이므로 미리 넣어준다.
# 0은 크기(n)과 인덱스를 같게 하기 위해 하나 추가해줌
memo = [0, 1, 3] + [0 for _ in range(28)]

def paper_use(n):
    global memo     # 경우의 수가 저장되어있는 memo 사용하기 위함

    # n에 값이 비어있다면 규칙을 이용해 넣어준다
    # 그런데 n-2, n-1에도 값이 비어있다 ? 그럼 재귀를 이용해 들어가서 계속 구한다.
    # (n = 3 부터 쭉 채우게 된다)
    if not memo[n]:
        memo[n] = 2 * paper_use(n-2) + paper_use(n-1)

    # memo[n]에 경우의 수가 저장되어있다면 바로 반환
    return memo[n]



t = int(input())

for t in range(1, t+1):
    n = int(input())//10    # 경우의 수와 인덱스로 편하게 이용하기 위해 //10 해줌
    print('#{} {}'.format(t, paper_use(n)))

