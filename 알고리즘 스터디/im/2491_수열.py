import sys
sys.stdin = open('input.txt')

n = int(input())    # 숫자의 개수
numbers = list(map(int, input().split()))   # 숫자들

small = [1 for _ in range(n)]   # 연속해서 작아지는 수열의 길이를 담을 리스트 (길이는 1이 기본. 왜냐면 숫자 1개의 길이가 1이니까)
big = [1 for _ in range(n)]     # 연속해서 커지는 수열의 길이를 담을 리스트

answer = 1  # 가장 긴 길이를 담을 변수

for i in range(1, n):
    # 만약 이전 숫자가 현재 숫자보다 작거나 같다면 연속해서 작아지는 경우이므로
    # 이전의 길이 +1 해서 넣어준다.
    if numbers[i] <= numbers[i-1]:
        temp = small[i-1] + 1
        small[i] = temp
        # 저장되어 있는 길이보다 길어졌다면 갱신
        if answer < temp:
            answer = temp

    # 만약 이전 숫자가 현재 숫자보다 크거나 같다면 연속해서 커지는 경우이므로
    # 이전의 길이 +1 해서 넣어준다.
    if numbers[i] >= numbers[i-1]:
        temp = big[i-1] + 1
        big[i] = temp
        # 저장되어 있는 길이보다 길어졌다면 갱신
        if answer < temp:
            answer = temp

print(answer)  # 저장되어있는 길이 출력