import sys
sys.stdin = open('input.txt')

n = int(input())    # 학생의 수
students = list(map(int, input().split()))  # 학생들이 뽑은 번호
answer = []

for i in range(n):
    # 현재까지 학생(i) - 번호 => i+1 학생이 들어갈 인덱스 자리
    # (4번 학생이 1번뽑으면 3-1=2번 인덱스에 들어간다)
    answer.insert(i-students[i], i+1)

print(*answer)