import sys
sys.stdin = open('input.txt')

n = int(input())

arr = [0 for _ in range(101)]
arr[1] = 1
arr[2] = 2

for i in range(3, n+1):
    # 규칙 : 현재 수 = 전의 수 + 전전 수
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])


