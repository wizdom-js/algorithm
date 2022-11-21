from collections import deque

word_l = 0


# 해당 단어로 변환 가능한지 검토 (알파벳 한 개만 다른지 검토)
def possible_change(before_word, after_word):
    diff = 0
    for i in range(word_l):
        if before_word[i] != after_word[i]:
            diff += 1

    if diff == 1:   # 알파벳 한 개만 다르다면
        return True
    return False


def solution(begin, target, words):
    global word_l

    word_n = len(words)
    word_l = len(words[0])

    queue = deque([[begin, 0]])

    visited = [0 for _ in range(word_n)]
    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt

        for i in range(word_n):
            if not visited[i]:  # 해당 단어로 변환한 적 없는 경우
                if possible_change(word, words[i]):
                    visited[i] = True
                    queue.append([words[i], cnt + 1])

    return 0    # 변환할 수 없는 경우
