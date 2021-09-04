import sys
sys.stdin = open('input.txt')

n = int(input())

arr = [0 for _ in range(1000001)]
arr[1] = 1
arr[2] = 2

for i in range(3, n):
    # 더해서 저장하고 마지막에 나머지 구하면 숫자가 너무 커지니, 나머지로 넣어준다.
    arr[i] = (arr[i-1] + arr[i-2]) % 15746

print(arr[(n)])