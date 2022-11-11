from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    word_n = len(words)

    queue = deque([[begin, 0]])

    while queue:
        x, cnt = queue.popleft()

        if x == target:
            return cnt

        for i in range(word_n):
            diff = 0
            word = words[i]
            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                queue.append([word, cnt + 1])
    return 0