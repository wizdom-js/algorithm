def solution(n, words):
    people = [0 for _ in range(n)]
    said_words = []
    last_word = words[0][0]
    for i in range(len(words)):
        word = words[i]
        people[i%n] += 1
        if word in said_words or word[0] != last_word:
            return [i%n+1, people[i%n]]
        else:
            said_words.append(word)
            last_word = word[-1]
    else:
        return [0, 0]