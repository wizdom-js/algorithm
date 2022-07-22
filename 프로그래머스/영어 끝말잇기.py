def solution(n, words):
    said_words = [] # 이미 말한 단어들
    last_word = words[0][0] # 처음 시작할 스펠링 (for문안에서 조건문(i != 0) 한번 더 쓰는거 방지하기 위함)
    for i in range(len(words)):
        word = words[i]
        if word in said_words or word[0] != last_word:  # 현재 단어가 이미 말한 단어이거나 끝 스펠링으로 시작하지 않은 경우
            return [i%n+1, i//n+1]  # [번호, 차례] return
        else:   # 끝말잇기가 맞는 경우
            said_words.append(word) # 이미 말한 단어에 추가
            last_word = word[-1]    # 끝 스펠링 바꾸기

    return [0, 0]   # 탈락자가 생기지 않은 경우 