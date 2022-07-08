import sys
sys.stdin = open('input.txt')

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(lotto)):
        combi[depth] = lotto[i]
        dfs(i + 1, depth + 1)

combi = [0 for i in range(13)]

while True:
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:
        break

    n = test_case[0]
    lotto = test_case[1:]
    dfs(0, 0)
    print()
