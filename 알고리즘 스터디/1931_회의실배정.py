import sys
sys.stdin = open('input.txt')

#### 다시 풀어보기

n = int(input())

# 회의 시간표 넣을 리스트. (튜플로 묶어준다.)
time = []
for _ in range(n):
    time.append(tuple(map(int, input().split())))

# 회의 끝나는 시간, 그다음은 회의 시작시간을 기준으로 오름차순 정렬
# 빨리끝나는 회의를 앞으로 둬야 계산을 많이 해볼 수 있기 때문이다. 예. (0, 10) (1, 3) (3, 9)
# 그리고 끝나는 시간이 같을 경우, 시작시간이 빠른걸 앞으로 배치한다.(시작하자마자 끝나는 경우때문) 예. (1, 3) (3, 3)
time.sort(key=lambda x: (x[1], x[0]))

answer = 0
end = 0
for s, e in time:
    # 현 미팅의 시작시간이 저장된 회의의 끝나는 시간과 안겹치는 경우
    if end <= s:
        answer += 1 # 정답 +1
        end = e     # 회의 끝나는 시간 변경

print(answer)





'''
9 
8 8 
5 8
3 4
2 5 
2 7
8 8
1 10
3 3
10 10

15
1 4
7 7
3 5
0 6
5 7
3 8
5 9
6 10
8 12
8 11
8 10
7 7
7 7
7 7
2 13
12 14

4
1 2
2 4
2 3
3 5

2
3 3
1 4

3
3 5
1 4
4 8
'''