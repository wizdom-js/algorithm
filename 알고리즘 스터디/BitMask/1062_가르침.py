import sys
sys.stdin = open('input.txt')

# dy = [1, -1, 0, 0]
# dx = [0, 0, 1, -1]

n, k = map(int, input().split())
words = [list(set(input())) for _ in range(n)]
# word_mx_idx = [0 for _ in range(n)]
# for i in range(n):
#     word_mx_idx[i] = len(words[i])-1

visit = 0
for word in ['a', 'c', 'i', 'n', 't']:
    visit |= (1 << (ord(word) - 97))

answer = 0
def read_cnt(visit):
    cnt = 0
    for i in range(n):
        for w in words[i]:
            if not visit & (1 << (ord(w) - 97)):
                break
        else:
            cnt += 1

    return cnt

def dfs(idx, cnt, visit):
    global answer

    if cnt == k-5:
        tmp = read_cnt(visit)
        if answer < tmp:
            answer = tmp
        return

    for i in range(idx, 26):
        bit = 1 << i
        if visit & bit:
            continue
        dfs(i, cnt + 1, visit | bit)
        # visit &= ~bit

dfs(0, 0, visit)
print(answer)


# for i in range(4):
#     ny = y + dy[i]
#     nx = x + dx[i]
#     if 0 <= ny < n and 0 <= nx < word_mx_idx[ny]:
#         bit = (1 << (ord(words[ny][nx]) - 97))
#         words[ny][nx] = 0
#         if visit & bit:
#             # if words[ny][nx]:
#             #     words[ny][nx] = 0
#             continue
#         dfs(ny, nx, cnt + 1, visit | bit)
#         visit &= ~bit
#         words[ny][nx] = chr(bit + 96)
