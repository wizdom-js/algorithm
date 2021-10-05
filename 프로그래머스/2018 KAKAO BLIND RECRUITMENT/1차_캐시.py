def solution(cacheSize, cities):
    cities = list(map(lambda x: x.lower(), cities))
    time = 0
    cache = []
    for city in cities:
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            cache.append(city)
            if cacheSize < len(cache):
                del cache[0]

    return time


####################################################
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
