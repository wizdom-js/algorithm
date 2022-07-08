import sys
sys.stdin = open('input.txt')

def dfs(s, depth):
    if depth == 6:
        print(*combination)
        return

    for i in range(s, k):
        combination[depth] = numbers[i]
        dfs(i+1, depth+1)


combination = [0 for _ in range(6)]

while True:
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:
        break

    k = test_case[0]
    numbers = test_case[1:]

    dfs(0, 0)
    print()