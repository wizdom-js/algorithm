import sys
sys.stdin = open('input.txt')

import heapq

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort()

meeting_rooms = [meetings[0][1]]
for meeting in meetings[1:]:
    # if meeting[0] >= meeting_rooms[0]:
    #     heapq.heappop(meeting_rooms)
    # heapq.heappush(meeting_rooms, meeting[1])

    # heapreplace => heappush, heappop 두 연산을 하는 것보다 효율적이다. 
    if meeting[0] < meeting_rooms[0]:
        heapq.heappush(meeting_rooms, meeting[1])
    else:
        heapq.heapreplace(meeting_rooms, meeting[1])

print(len(meeting_rooms))
