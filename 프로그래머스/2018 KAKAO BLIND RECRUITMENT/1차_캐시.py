def solution(cacheSize, cities):
    cities = list(map(lambda x: x.lower(), cities)) # 다 소문자 변환
    time = 0
    cache = []
    for city in cities:
        if city in cache:   # cache hit인 경우
            time += 1
            cache.remove(city)  # LRU 이므로 캐시 리스트 맨 마지막으로 갱신시킨다.
            cache.append(city)
        else:               # cache miss인 경우
            time += 5
            cache.append(city)
            if cacheSize < len(cache):  # cache가 다 채워지지 않는 경우도 있으므로 조건문 달아줘야함
                del cache[0]

    return time


###################### deque 사용해서 풀어봄 근데 더 느렸음 ###############################
import collections


def solution(cacheSize, cities):
    cities = list(map(lambda x: x.lower(), cities))
    time = 0
    cache = collections.deque(maxlen=cacheSize)
    for city in cities:
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            cache.append(city)

    return time
