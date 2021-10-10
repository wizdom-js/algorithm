import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    dict = {}
    for _ in range(1, N+1):
        inp = tuple(input().split())
        dict[int(inp[0])] = inp[1:]

    for idx in range(N, 0, -1):
        if dict[idx][0].isdigit():
            dict[idx] = int(dict[idx][0])
        else:
            if dict[idx][0] == '+':
                dict[idx] = dict[int(dict[idx][1])]+dict[int(dict[idx][2])]
            elif dict[idx][0] == '-':
                dict[idx] = dict[int(dict[idx][1])]-dict[int(dict[idx][2])]
            elif dict[idx][0] == '*':
                dict[idx] = dict[int(dict[idx][1])]*dict[int(dict[idx][2])]
            elif dict[idx][0] == '/':
                dict[idx] = dict[int(dict[idx][1])]//dict[int(dict[idx][2])]

    print('#{} {}'.format(tc, dict[1]))
