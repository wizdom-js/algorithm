def solution(citations):
    citations.sort()

    hIndex_up = len(citations) - 1
    hIndex_down = 0
    hIndex_idx = 0
    for c in citations[1:]:
        if c < citations[hIndex_idx]:
            hIndex_down += 1
        if c > citations[hIndex_idx]:
            hIndex_up += 1

        if hIndex_down > hIndex_up:
            break

    return citations[hIndex_idx]
