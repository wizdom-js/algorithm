import sys
sys.stdin = open('input.txt')


n, m = map(int, input().split())
arr = [0 for _ in range(n)]
visited = [False for _ in range(n)]

def recur(num):
    if num == m:
        print(arr)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr[num] = i
            recur(num + 1)
            visited[i] = False

recur(0)
